---
title: "Differential co-expression-based detection of conditional relationships in transcriptional data: comparative analysis and application to breast cancer"
authors:
- admin
- Joseph Cursons
- Gordon K Smyth
- Melissa J Davis
date: "2019-11-14"
doi: "https://doi.org/10.1186/s13059-019-1851-8"

# Schedule page publish date (NOT publication's date).
publishDate: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "Genome Biology"
publication_short: "Genome Biol."

abstract: "Background: Elucidation of regulatory networks, including identification of regulatory mechanisms specific to a given biological context, is a key aim in systems biology. This has motivated the move from co-expression to differential co-expression analysis and numerous methods have been developed subsequently to address this task; however, evaluation of methods and interpretation of the resulting networks has been hindered by the lack of known context-specific regulatory interactions.

Results: In this study, we develop a simulator based on dynamical systems modelling capable of simulating differential co-expression patterns. With the simulator and an evaluation framework, we benchmark and characterise the performance of inference methods. Defining three different levels of “true” networks for each simulation, we show that accurate inference of causation is difficult for all methods, compared to inference of associations. We show that a z-score-based method has the best general performance. Further, analysis of simulation parameters reveals five network and simulation properties that explained the performance of methods. The evaluation framework and inference methods used in this study are available in the dcanr R/Bioconductor package.

Conclusions: Our analysis of networks inferred from simulated data show that hub nodes are more likely to be differentially regulated targets than transcription factors. Based on this observation, we propose an interpretation of the inferred differential network that can reconstruct a putative causal network."

# Summary. An optional shortened abstract.
summary: dcanr is a method that helps infer differential regulatory networks from high-througput 'omics data

tags:
- networks
- regulatory networks
- differential co-expression
featured: false

links:
- name: Bioconductor
  url: https://www.bioconductor.org/packages/release/bioc/html/dcanr.html
url_pdf: 'https://genomebiology.biomedcentral.com/counter/pdf/10.1186/s13059-019-1851-8.pdf'
url_code: 'https://github.com/DavisLaboratory/dcanr'
url_dataset: 'https://doi.org/10.26188/5cb8049f593a6'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'An immune-related regulatory module regulated specifically in estrogen receptor negative breast cancers'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
