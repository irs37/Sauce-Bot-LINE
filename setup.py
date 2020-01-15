# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['handlers', 'handlers.Roboragi', 'handlers.nHentaiTagBot', 'handlers.sauce']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4==4.8.1',
 'cachecontrol==0.12.5',
 'cachetools==3.1.1',
 'certifi==2019.11.28',
 'chardet==3.0.4',
 'click==7.0',
 'cloudinary==1.18.2',
 'colorclass==2.2.0',
 'cssselect==1.1.0',
 'decorator==4.4.1',
 'docopt==0.6.2',
 'firebase-admin==3.2.0',
 'flask==1.1.1',
 'future==0.18.2',
 'google-api-core==1.14.3',
 'google-api-python-client==1.7.11',
 'google-auth-httplib2==0.0.3',
 'google-auth==1.7.1',
 'google-cloud-core==1.0.3',
 'google-cloud-firestore==1.6.0',
 'google-cloud-storage==1.23.0',
 'google-resumable-media==0.5.0',
 'googleapis-common-protos==1.6.0',
 'grpcio==1.25.0',
 'httplib2==0.14.0',
 'idna==2.8',
 'imageio-ffmpeg==0.3.0',
 'imageio==2.6.1',
 'itsdangerous==1.1.0',
 'jinja2==2.10.3',
 'line-bot-sdk==1.15.0',
 'lxml==4.4.2',
 'markupsafe==1.1.1',
 'mock==3.0.5',
 'msgpack==0.6.2',
 'numpy==1.17.4',
 'opencv-python-headless==4.1.2.30',
 'packaging==19.2',
 'pillow==6.2.1',
 'pip-upgrader==1.4.15',
 'proglog==0.1.9',
 'protobuf==3.11.0',
 'pyasn1-modules==0.2.7',
 'pyasn1==0.4.8',
 'pyparsing==2.4.5',
 'pyquery==1.4.1',
 'pytz==2019.3',
 'requests==2.22.0',
 'rsa==4.0',
 'six==1.13.0',
 'soupsieve==1.9.5',
 'terminaltables==3.1.0',
 'tqdm==4.40.0',
 'uritemplate==3.0.0',
 'urllib3==1.25.7',
 'werkzeug==0.16.0']

setup_kwargs = {
    'name': 'handlers',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)