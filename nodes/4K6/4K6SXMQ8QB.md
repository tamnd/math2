---
tag: 4K6SXMQ8QB
kind: definition
name: Julian day
msc: [85A04]
defines: DWS7SD01BS
sources:
  - url: https://en.wikipedia.org/wiki/Julian_day
---

## Definition

The *Julian day number* of a day is the number of whole days elapsed since the epoch.
The epoch is noon Universal Time on 1 January 4713 BC of the proleptic Julian calendar.
This is year $-4712$ in astronomical numbering.
The day with Julian day number $0$ begins at the epoch.
The *Julian date* of an instant is the Julian day number of its day plus the fraction of a day elapsed since the preceding noon.

## Remarks

Julian days begin at noon, not at midnight, so a night of observations has a single Julian day number.
Example: the instant 1 January 2000, 12:00, has Julian date $2\,451\,545.0$; this is the standard epoch J2000.0, in the time scale TT.
Example: 1 January 1970, 0:00 UT, has Julian date $2\,440\,587.5$; the fraction $.5$ is half a day after the preceding noon.
Non-example: a date such as 1 January 2000 in the Gregorian calendar is not a Julian date; it is a calendar date that must be converted.
The *modified Julian date* is $\mathrm{MJD} = \mathrm{JD} - 2\,400\,000.5$; it starts at midnight.
The Julian day has nothing to do with the Julian calendar except that the epoch is expressed in it.
