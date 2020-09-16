docker build -t local/autorestpython .

generated_code_dir="../sdk/src/microsoft/marketplace"

if [[ -d $generated_code_dir ]]; then
    echo "Cleaning out previously generated files"
    rm -rf "$generated_code_dir/meter"
    rm -rf "$generated_code_dir/saas"
fi

mkdir -p "../sdk/src/"

current_dir=$(pwd)

docker run --rm --name pythonautorest \
    -v $current_dir/temp/saas:/out \
    -v $current_dir:/input \
    local/autorestpython \
    --input-file:/input/saasapi.v2.json \
    --v3 \
    --python \
    --use:@autorest/python@5.3.2 \
    --output-folder:/out  \
    --add-credentials \
    --namespace:microsoft.marketplace.saas \
    --verbose \
    --clear-output-folder:true \
    --public-clients:true \
    --license-header:MICROSOFT_MIT_NO_VERSION \
    --credential-scopes=20e940b3-4c77-4b0b-9a53-9e16a1b010a7/.default

docker run --rm --name pythonautorest \
    -v $current_dir/temp/meter:/out \
    -v $current_dir:/input \
    local/autorestpython \
    --input-file:/input/meteringapi.v1.json \
    --v3 \
    --python \
    --use:@autorest/python@5.3.2 \
    --output-folder:/out  \
    --add-credentials \
    --namespace:microsoft.marketplace.meter \
    --verbose \
    --clear-output-folder:true \
    --public-clients:true \
    --license-header:MICROSOFT_MIT_NO_VERSION \
    --credential-scopes=20e940b3-4c77-4b0b-9a53-9e16a1b010a7/.default

cp -r ./temp/meter/* ../sdk/src
cp -r ./temp/saas/* ../sdk/src
