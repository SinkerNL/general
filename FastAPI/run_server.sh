#!/bin/bash
RUNWITHPOSTGRES="$1"

main() 
{
    if [ $RUNWITHPOSTGRES = "1" ]; then
        # Run the uvicurn app and auto reload based on save
        uvicorn app.main_with_db:app --reload
    else
        uvicorn app.main:app --reload
    fi
}

main