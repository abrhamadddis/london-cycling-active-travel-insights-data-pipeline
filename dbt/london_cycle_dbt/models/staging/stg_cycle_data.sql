{{ config(materialized='view') }}

SELECT
  wave,
  site_id,
  -- Combine date and time into a TIMESTAMP column
  PARSE_TIMESTAMP(
    '%d/%m/%Y %H:%M:%S',
    CONCAT(date, ' ', time)
  ) AS date_time,
  weather,
  day,
  round,
  direction,
  mode,
  count
FROM {{ source('raw_data', 'raw_cycle_data') }}