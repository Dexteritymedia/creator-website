{% load static %}
{% autoescape off %}
importScripts("{% static 'service-worker.js' %}");
{% endautoescape %}