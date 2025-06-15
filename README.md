# CSV-2-JSON Transformer ![Static Badge](https://img.shields.io/badge/status-WIP-blue)
### CSV to JSON inter-transformer built in Angular & FastAPI, leveraging Gemini AI API via LangChain.

A simple application that transforms a CSV file to JSON, and a JSON array request to a CSV file. While FastAPI exposes REST API to accept requests of these payloads and return the transformed counter representation, the entire operation that runs the transformation is delegated to Google's Gemini AI - Flash 2.0. LangChain (v0.3) equipped with Gemini's SDK serves as the adapter to the LLM, handling the integration with Gemini. 

#### The Architecture
<img src="docs/architecture.png"></img>

#### Note
There are possibly much efficient and smarter ways to interact with the LLM - such as uploading the CSV file directly via `HumanMessage` from LangChain than what has been implemented so far. We will incrementally update the codebase with such improvisations as I understand more about LangChain and its capabilities. However, the first _POC_ version will be proclaimed complete with the basic implementation (including the Angular application), and will have gradual communication optimizations with the LLM.
