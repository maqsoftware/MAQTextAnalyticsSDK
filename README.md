---
# Text Analytics SDK Documentation
by **MAQ Software**

[Privacy Policy][PP]
---
## Prerequisites
> Requires Python 3.6 or above
## Installation
```sh
$ pip install MAQTextSDK
```
## Getting Started with SDK
#### 1. Register for the SDK
You need an O365 Account to register.
   * Click [here][PlDb] to register using the *Free Trial* button in the *Developer Zone* pane. 
   * Save the **API Endpoint** and **API Key** you receive while registering on the *Developer Zone* pane.
#### 2. Install the SDK
```sh
$ pip install MAQTextSDK
```
#### 3. Using the SDK
   * Load the *Corpus* you plan to use in a *List* format, as shown in the following code snippet:
```sh
$ corpus = ['I love working on ML stuff.'
          ,'I hate working on stuff that is boring and repetitive.'
          ,'I love working from home during COVID-19.']
```
   * Use the **API Key** and **API Endpoint** you received while registering on the *Developer Zone* pane, as shown in the following code snippet:
```sh
$ APIKey = "Your_API_Key"
$ APIEndpoint = "Your_API_Endpoint"
````
   * Import the SDK and pass the *Corpus* along with the **API Endpoint** and **API Key**, as shown in the following code snippet:
```sh
$ import  MAQTextSDK.maq_text_analytics_linux as SentimentSDK
$ sentimentClient = SentimentSDK.MAQTextAnalyticsLinux(base_url = APIEndpoint)

$ response = sentimentClient.post_sentimentclassifier(api_key = APIKey, data_input = corpus)

$ for document in response:
    print("Document:")
    print(document['text'])
    print("Sentiment:")
    print(document['sentiment'])
    print()
````

## Using the Requests Package
   * Load the *Corpus* you plan to use in a Json format, as shown in the following code snippet:
```sh
$ corpus = {"data": [
    {"id": "1", "text": "I love working on ML stuff."},
    {"id": "2", "text": "I hate working on stuff that is boring and repetitive."},
    {"id": "3", "text": "I love working from home in COVID-19."}
]}
```
   * Input the **API Key** and **API Endpoint** that you received when you registered on the Text Analytics Platform, as shown in the following code snippet:
```sh
$ APIKey = "Your_API_Key"
$ APIEndpoint = "Your_API_Endpoint"
$ headers = {"APIKey": APIKey}
````
   * Import the Requests library and pass the *Corpus*, **API Endpoint**, and **Headers** into the Json parameter, as shown in the following code snippet:
```sh
$ import requests

$ response = requests.post(APIEndpoint + "/SentimentClassifier", headers = headers, json = corpus)
$ sentiment = response.json()
````
## Limit Tracking in API
In the free trial subscription, the API Key has a default quota of 500 batch calls. In a single batch call, you can send maximum 25 documents. Each batch call, irrespective of the how many documents it processes, counts as a single call.

## Build the SDK
To build the SDK from scratch. Please use *MAQTextAnalyticsLinux.swagger.json* file and build it using *[autorest][autorestLink]*. To build the SDK package please run the following code snippet:
```sh
$ git clone https://github.com/maqsoftware/MAQTextAnalyticsSDK.git
$ npm install -g autorest
$ autorest --input-file="MAQTextAnalyticsSDK/MAQTextAnalyticsLinux.swagger.json" --python --output-folder="TextAnalyticsSDK"
````
## FAQs

1. **What happens when my API Key expires?**
You can re-register for a free trial subscription by clicking [here][PlDb]. For more information, you can connect with us at support@maqsoftware.com.

    
2. **What happens when my API Limit is exhausted?**
    You will get an API Limit exceeded error when you try to use the SDK. You can visit the *Developer Zone* pane and generate a new API Key. For a premium service, you can connect with us at support@maqsoftware.com

3.	**Why I am getting batch size error?**
You can send maximum 25 documents in a single batch call. Check that you are not trying to send more.


[PlDb]: <https://textanalytics.maqsoftware.com/>
[PP]: <https://maqsoftware.com/privacystatement>
[autorestLink]: <https://github.com/Azure/autorest>
