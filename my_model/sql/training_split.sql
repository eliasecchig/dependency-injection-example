SELECT
  {% for column in (id_columns + numeric_features + target_features) %}
    {{ column }},
  {% endfor %}
FROM
  `{{ training_features_table }}`
WHERE
...
