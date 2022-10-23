# surfs_up.

## Overview of Analysis

The purpose of this analysis was to extract weather data from a SQLite file to be able to understand June and December weather trends. Because the data is living in a database, we had to properly read in the file using pandas methods as well as SQLAlchemy. By running a query to get the dates and temperatures, we were able to convert this query to a list to then put into a dataframe. Once the data was properly stored in a dataframe, we used pandas .describe() to understand summary statistics.

## Results 

Based on our summary statistics for June and December, we can discern the following:
- The max temp for for June and December are not very different (85 degrees and 83 degrees, respectively), however, the minumum ranges from 64 degrees in June to 56 degrees in December. This isn't surprising knowing that December is a winter month.
- It is interesting to know that the average temperature for each month only varies by three degrees, as June has an average temperatue of 74.9 and December has an average temperatue of 71. Sounds like both months are ideal for ice cream eating!
- Its also interesting to note that the month of June has more data - specifically 1,800 instances of data, whereas December has 1,517 instances, indiciating that if each month was on par with the amount of data collected, December numbers could shift a bit.

## Summary

Overall, June and December are optimal months to sell ice cream. December might prove to be a slower month only because it does get colder, but based on temperature data there is no reason to believe that December would lag too far behind June in terms of ice cream sales.

We could perform more queries to understand a little more about the weather data for each month. One query we could run would be to replace the Measurement table with the Station table to understand discrepancies in reporting data. The query would look like this for the month of December:

results_stations = session.query(Station.date, Station.tobs).filter(Station.date.like('%-12-%'))

Another query we could perform to learn more about June and December weather data would be to pull in data from other months. This way, we could understand the summary statistics of months between June and December to uncover more trends. The more trends we understand, the more we can predict how we should be preparing and running our business.

There are multiple queries we could run here, but an example to figure out summary stats for the month of October, for example, would look like this:

results_october = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date.like('%-10-%'))

