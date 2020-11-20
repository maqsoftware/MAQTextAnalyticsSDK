from distutils.core import setup
setup(
  name = 'MAQTextSDK',         
  packages = ['MAQTextSDK','MAQTextSDK.models'],  
  version = '0.1',      
  license='MIT', 
  description = 'NLP based text processing SDK', 
  author = 'MAQ',                  
  author_email = 'support@maqsoftware.com',    
  url = 'https://github.com/maqsoftware/MAQTextAnalyticsSDK',   
  download_url = 'https://github.com/maqsoftware/MAQTextAnalyticsSDK/archive/v_1.tar.gz',  
  keywords = ['NLP', 'Text', 'Sentiment'], 
  install_requires=[          
    'msrest'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',    
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
