from setuptools import setup, find_packages

setup(
    name='azuremarketplace',
    version='0.9.1',    
    description='The Microsoft commercial marketplace SaaS offer billing SDK enables Partners and Startups to build the requirements for the implementation of transactable SaaS offers for both the AppSource and Azure Marketplaces.',
    url='https://github.com/Azure/commercial-marketplace-client-python',
    author='Scott Seely',
    author_email='scott@scottseely.com',
    license='MIT',
    packages=find_packages(exclude=[
        'test',
    ]),
    install_requires=['msal',
                      'azure-core',
                      'azure-identity',
                      'azure-mgmt-subscription',
                      'azure-mgmt-resource',
                      'msrest',
                      ],
    project_urls={
        'Source': 'https://github.com/Azure/commercial-marketplace-client-python',
        'Tracker': 'https://github.com/Azure/commercial-marketplace-client-python/issues',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)