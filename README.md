# timeseries

## Backend 
- Provide REST API that accepts JSON in the following format

### JSON Model
```
timestamps = [
    {
        timestamp: value,
        y: value,
    },
    {
        timestamp: value,
        y: value,
    }
]
```

## Frontend
- Allows user to upload CSV with the folowing columns: timestamp, y
- We then take the csv clean the data on the client 
- Cleaned data is sent to backend where a N day forecast is generated and returned in the response
- Plot results on chart

