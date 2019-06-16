---
layout: page
permalink: /cv.html
title: cv
published: false
---

<div class="cv-pdf">
	<a href="/assets/pdf/vitae.pdf" target="_blank">
	  <img height="60px" src="/assets/img/pdf_icon.png">
	  <p>PDF</p>
	</a>
</div>

<div class="cv">
{% for entry in site.data.cv %}
  <h3>{{ entry.title }}</h3>
  <div>
	{% if entry.type == "list" %}
	  <ul class="list">
		{% for content in entry.contents %}
		  <li>{{ content}}</li>
		{% endfor %}
	  </ul>
  {% elsif entry.type == "map" %}
	  <table class="map">
		{% for content in entry.contents %}
			<tr>
		  <td><b>{{ content.name }}</b></td>
		  <td>{{ content.value }}</td>
		  </tr>
		{% endfor %}
	  </table>
  {% elsif entry.type == "table" %}
	  <ul class="table">
		{% for content in entry.contents %}
			{% if content.location %}
		    <h3 class="location">{{ content.location }}</h3>
		  {% endif %}
		  <li class="table-row">
		  {% if content.year %}
		    <span class="year">{{ content.year }}</span>
		  {% endif %}
		  	<div>
		  		{% if content.title %}
				  	{% if content.description %}
				  	    <span class="title">{{content.title}}</span>
					  	<ul class="items">
                        {% for item in content.description %}
                          <li>
                            {% if item.contents %}
                                <span class="item-title">{{ item.title }}</span>
                                <ul class="subitems">
                                    {% for subitem in item.contents %}
                                      <li><span class="subitem">{{ subitem }}</span></li>
                                    {% endfor %}
                                    </ul>
                            {% else %}
                                <span class="item">{{ item }}</span>
                            {% endif %}
                          </li>
                        {% endfor %}
					  	</ul>
				  	{% else %}
                        <span class="plain-title">{{content.title}}</span>
				  	{% endif %}
				  {% else %}
				    <ul class="items">
                    {% for item in content.items %}
                      <li>
                        {% if item.contents %}
                            <span class="item-title">{{ item.title }}</span>
                            <ul class="subitems">
                                {% for subitem in item.contents %}
                                  <li><span class="subitem">{{ subitem }}</span></li>
                                {% endfor %}
                                </ul>
                        {% else %}
                            <span class="item">{{ item }}</span>
                        {% endif %}
                      </li>
                    {% endfor %}
				  	</ul>
				  {% endif %}
			  </div>
		  </li>
		{% endfor %}
	  </ul>
  {% endif %}
  </div>
{% endfor %}
</div>
