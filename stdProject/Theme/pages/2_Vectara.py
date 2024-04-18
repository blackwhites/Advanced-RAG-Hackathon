import json
import requests
import streamlit as st

api_key = "zqt_ve623_C4RxPjS-H5dE0U3x5Q0_6FfYIPGXjYGQ"
corpus_id = "3"
customer_id = "3186538207" 
import streamlit as st

# Change the title color using HTML formatting with hexadecimal color code
st.markdown("<h1 style='color: #611349;'> 📃 Vectara's Advanced Search</h1>", unsafe_allow_html=True)
# Define the search term input field
search_term = st.text_input("Enter a search term:", placeholder="Enter your search term here")

if search_term:
    url = "https://api.vectara.io:443/v1/query"
    headers = {
        "x-api-key": api_key,
        "customer-id": customer_id
    }
    
    payload = {
        "query": [
            {
                "query": search_term,
                "queryContext": "",
                "start": 0,
                "numResults": 10,
                "contextConfig": {
                    "charsBefore": 0,
                    "charsAfter": 0,
                    "sentencesBefore": 2,
                    "sentencesAfter": 2,
                    "startTag": "%START_SNIPPET%",
                    "endTag": "%END_SNIPPET%"
                },
                "corpusKey": [
                    {
                        "customerId": customer_id,
                        "corpusId": corpus_id,
                        "semantics": 0,
                        "metadataFilter": "",
                        "lexicalInterpolationConfig": {
                            "lambda": 0.025
                        },
                        "dim": []
                    }
                ],
                "summary": [
                    {
                        "maxSummarizedResults": 5,
                        "responseLang": "eng",
                        "summarizerPromptName": "vectara-summary-ext-v1.2.0"
                    }
                ]
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Check if the response is successful
    if response.status_code == 200:
        search_results = response.json()
        
        # Extract and display search results
        if "responseSet" in search_results:
            summary = search_results["responseSet"][0]["summary"][0]["text"]
            st.markdown("<h1 style='color: #611349;'> Summary</h1>", unsafe_allow_html=True)
            st.write(summary)
    
            documents = search_results["responseSet"][0]["document"]
            for i, el in enumerate(search_results["responseSet"][0]["response"]):
                st.caption("["+str(i+1)+"] "+documents[el["documentIndex"]]["id"]+", "+str(el["score"]))
                st.write(" ".join(el["text"].split()).replace("*","").replace("%START_SNIPPET%","**").replace("%END_SNIPPET%","**"))
        else:
            st.error("No search results found.")
    else:
        st.error("Failed to fetch search results. Status code: {}".format(response.status_code))
