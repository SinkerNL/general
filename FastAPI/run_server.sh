#!/bin/bash

main() 
{
    # Run the uvicurn app and auto reload based on save
    uvicorn main:app --reload
}

main