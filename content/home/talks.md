---
# An instance of the Pages widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: portfolio

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 70

title: 'Recent & Upcoming Talks'
subtitle:

content:
  # Page type to display. E.g. post, event, publication...
  page_type: event
  # Choose how many pages you would like to display (0 = all pages)
  count: 5
  # Choose how many pages you would like to offset by
  offset: 0
  # Page order: descending (desc) or ascending (asc) date.
  order: desc
  # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  filter_default: 0
  filter_button:
    - name: All
      tag: '*'
    - name: Invited talks
      tag: invited talk
    - name: Workshops
      tag: workshop
    # - name: Keynotes
    #   tag: keynote

design:
  # Choose a view for the listings:
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  view: 2
---
