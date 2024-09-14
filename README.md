# ipltrivi-alloydb
Enable NL to SQL capabilities with AlloyDB Omni

<img width="679" alt="image" src="https://github.com/user-attachments/assets/3b973133-5a06-47ec-9d1b-2abd4ce35763">

## Steps to run IPL trivia
```
Create Extension
postgres@localhost:iplnew> \dx
+-----------------------+----------------+------------+------------------------------------------------------+
| Name                  | Version        | Schema     | Description                                          |
|-----------------------+----------------+------------+------------------------------------------------------|
| alloydb_ai_nl         | 1.0            | public     | Google Extension for AlloyDB AI & Natural Language   |
| google_db_advisor     | 1.0            | public     | Google extension for Database Advisor                |
| google_ml_integration | 1.3            | public     | Google extension for ML integration                  |
| hypopg                | 1.3.2          | public     | Hypothetical indexes for PostgreSQL                  |
| plpgsql               | 1.0            | pg_catalog | PL/pgSQL procedural language                         |
| vector                | 0.7.0.google-1 | public     | vector data type and ivfflat and hnsw access methods |
+-----------------------+----------------+------------+------------------------------------------------------+

Enable Flags 
 \dconfig alloydb_ai_nl.enabled|google_ml_integration.enable_model_support|shared_preload_libraries
                                                       List of configuration parameters
                 Parameter                  |                                              Value
--------------------------------------------+-------------------------------------------------------------------------------------------------
 alloydb_ai_nl.enabled                      | on
 google_ml_integration.enable_model_support | on
 shared_preload_libraries                   | g_stats,google_job_scheduler,google_insights,pg_stat_statements,google_db_advisor,alloydb_ai_nl
(3 rows)

Load Model

CALL google_ml.create_model(model_id => 'gemini-pro-text-to-sql'
        ,model_request_url => 'https://us-central1-aiplatform.googleapis.com/v1/projects/datacloudgaze/locations/us-central1/publishers/google/models/gemini-1.5-pro-001:streamGenerateContent',
        model_provider => 'google',model_auth_type => 'alloydb_service_agent_iam');

SELECT alloydb_ai_nl.google_get_sql_current_schema(sql_text => 'who scored most run in IPL Season 2024', model_id => 'gemini-pro-text-to-sql');
```
