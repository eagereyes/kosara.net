---
layout: page
permalink: /publications.html
title: publications
description: Robert's published papers
list: yes
years: [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010,
        2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000,
        1999, 1998]
---

{% for y in page.years %}
  <h3 class="bibliography-year">{{y}}</h3>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
