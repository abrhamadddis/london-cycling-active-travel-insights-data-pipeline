{{ config(materialized='table') }}

SELECT
  GENERATE_UUID() AS record_id,
  c.site_id,
  c.wave,
  c.date_time,
  EXTRACT(YEAR FROM c.date_time) AS year,
  EXTRACT(MONTH FROM c.date_time) AS month,
  EXTRACT(DAYOFWEEK FROM c.date_time) AS day_of_week,
  EXTRACT(HOUR FROM c.date_time) AS hour,
  c.weather,
  c.day,
  c.round,
  c.direction,
  c.mode,
  c.count,
  m.location_description,
  m.borough,
  m.functional_area,
  m.road_type,
  m.strategic_panel
FROM {{ ref('stg_cycle_data') }} c
LEFT JOIN {{ ref('stg_monitoring') }} m
  ON c.site_id = m.site_id