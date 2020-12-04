docker build -t local/autorestpython .

# Powershell up through 7.03 continues to have an issue with calling
# Remove-Item -Recurse 
# on folders that live in a OneDrive folder. The following code
# is functionally equivalent to Remove-Item and does not suffer
# from the bug.
function deleteFolder($folderName){
    $directories = Get-ChildItem $folderName -Directory

    Write-Host "Deleting folder $folderName"
    foreach($dir in $directories){
        deleteFolder($dir.FullName)
    }

    $files = Get-ChildItem $folderName -File

    foreach ($file in $files){
        Remove-Item $file.FullName
    }

    Remove-Item $folderName
}

$current_dir=(Get-Location).Path

$generated_code_dir="${current_dir}/../sdk/src/microsoft/marketplace"
$meter_path="${generated_code_dir}/meter"
$saas_path="${generated_code_dir}/saas"
$sdk_path="../sdk/src"

if (Test-Path -Path $generated_code_dir -PathType Container)
{
    Write-Host "Cleaning out previously generated files"
    if ($true -eq (Test-Path -Path $meter_path -PathType Container))
    {
        Write-Host "Clearing out $meter_path"
        deleteFolder($meter_path)
    }
    if ($true -eq (Test-Path -Path $saas_path -PathType Container))
    {
        Write-Host "Clearing out $saas_path"
        deleteFolder($saas_path)
    }
}

#return

if (-Not (Test-Path -Path $sdk_path -PathType Container))
{
    New-Item -Path $sdk_path -Force
}

docker run --rm --name pythonautorest `
    -v ${current_dir}/temp/saas:/out `
    -v ${current_dir}:/input `
    local/autorestpython `
    --input-file:/input/saasapi.v2.json `
    --v3 `
    --python `
    --use:@autorest/python@5.3.2 `
    --output-folder:/out  `
    --add-credentials `
    --namespace:microsoft.marketplace.saas `
    --verbose `
    --clear-output-folder:true `
    --public-clients:true `
    --license-header:MICROSOFT_MIT_NO_VERSION `
    --credential-scopes=20e940b3-4c77-4b0b-9a53-9e16a1b010a7/.default

docker run --rm --name pythonautorest `
    -v ${current_dir}/temp/meter:/out `
    -v ${current_dir}:/input `
    local/autorestpython `
    --input-file:/input/meteringapi.v1.json `
    --v3 `
    --python `
    --use:@autorest/python@5.3.2 `
    --output-folder:/out  `
    --add-credentials `
    --namespace:microsoft.marketplace.meter `
    --verbose `
    --clear-output-folder:true `
    --public-clients:true `
    --license-header:MICROSOFT_MIT_NO_VERSION `
    --credential-scopes=20e940b3-4c77-4b0b-9a53-9e16a1b010a7/.default

cp -r ./temp/meter/* ../sdk/src -Force
cp -r ./temp/saas/* ../sdk/src -Force
