#!/usr/bin/env python3

import os
import requests
import openai
from openai import OpenAI

# Print library versions
print(requests.__version__)
print(openai.__version__)

# Check API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("⚠️  Skipping Example 1: OPENAI_API_KEY not set")
    print("   Set with: export OPENAI_API_KEY='your-api-key-here'")
else:
    print("Hello, World!")

    # Initialize client
    client = OpenAI(api_key=api_key)

    # First response
    response = client.responses.create(
        model="gpt-5",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    print(response.output_text)

    # Second response
    response = client.responses.create(
        model="gpt-5",
        input="Continue the story for another two sentences, keeping the same animal."
    )
    print("Hello, World!")
    print(response.output_text)
