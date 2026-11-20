# Django Traffic Light Protocol

django-tlp is a small Django app for attaching a "traffic light" status (plus
an optional note) to any model instance via a GenericForeignKey, with an
htmx-based UI.

By default the traffic light allows the values to be red, orange, and green but
those choices are user configurable;

The app provides a templatetag that shows an interface element similar to a
traffic light. The traffic light allows one to change the traffic light status
using htmx; in addition, a note can be attached to the traffic light status.
The interface elements uses the configurable options to show different colored
circles; the colors of the options are the different choices values.
