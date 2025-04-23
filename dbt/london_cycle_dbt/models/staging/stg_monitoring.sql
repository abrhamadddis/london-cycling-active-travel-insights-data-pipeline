{{ config(materialized='view') }}

SELECT
  site_id,
  location_description,
  borough,
  functional_area,
  road_type,
  strategic_panel,
  old_site_id,
  latitude,
  longitude,
  CONCAT(latitude, ',', longitude) AS lat_lon
FROM {{ source('raw_data', 'monitoring_locations') }}