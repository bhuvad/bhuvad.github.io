---
title: 'vissE – Visualising higher-order biological processes in cancer ‘omics datasets'

event: 'Victorian Cancer Bioinformatics Symposium (VCBS) 2021'
event_url: ''

location: Online

summary: A talk on using vissE to analyse transcriptomic data
abstract: 'Gene-set enrichment analysis is a powerful bioinformatics tool to identify the functional processes underlying cancer systems. This analysis is often used to functionally annotate gene lists derived from a range of workflows including but not limited to differential expression analysis. Most analyses result in hundreds of significantly enriched gene-sets. Biologists are then tasked with sifting through these lists of gene-sets and extracting relevant knowledge pertaining to their experiment. The process of selecting gene-sets of interest from these results is typically heavily biased by the knowledge and expectations of the biologist and may miss results that could lead to novel hypotheses. To address this issue, I develop a network-based analysis method that clusters the numerous gene-sets identified from gene-set enrichment analyses into broader biological themes. I then automatically annotate gene-set clusters using text-mining approaches. Harnessing the benefits of network analyses, vissE maps the results of enrichment analysis thus allowing biologists to understand the significance of biological themes identified. Additionally, vissE visualises common genes across gene-set clusters thus providing a common view of both genes and gene-sets. I demonstrate the application of vissE in a breast cancer transcriptomic dataset where an epithelial to mesenchymal transition was induced using TGFb. VissE identified expected changes in the molecular phenotype of cells such as those associated with a mesenchymal transition. In addition to this, higher-order processes that represented interactions with the extra-cellular matrix were identified along with the genes involved. Without vissE, these processes would likely have remained buried in the long list of results. A vissE analysis can assist cancer biologists in identifying biological themes in their experiments to drive novel hypotheses. Visualisations generated using vissE combine gene-level statistics with condensed gene-set enrichment analysis results thus providing a more holistic view of the cancer system being investigated.'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2021-10-08'
#date_end: ''
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2021-10-08'

authors:
  - admin
tags:
  - gene-set enrichment analysis
  - molecular phenotypes
  - networks
  - breast cancer
  - EMT

# Is this a featured talk? (true/false)
featured: false

image:
  caption: ''
  focal_point: Right

links:
  - icon: twitter
    icon_pack: fab
    name: Follow
    url: https://twitter.com/bhuva_dd
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ''

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

# Lay summary

In normal tissue, biological processes such as cell growth and division are well regulated to ensure normal function. In cancer, this regulation can break down, contributing to tumour growth and spread. We can now measure all molecules in a cancerous cell to discover how cancer differs from normal tissue, but these experiments identify thousands of genes that are changed. We match genes back to high-level biological processes to understand the functional impact of these changes, but this still results in the identification of hundreds to thousands of altered processes.

Scientists naturally tend to focus on the top genes and processes, particularly if they are familiar or known to play a role in cancer, creating a real risk that new discoveries may be missed during manual candidate selection. To address this problem, I developed a method that automates the selection part of this interpretation. The method automatically groups related biological processes, interprets their combined biology using text-mining approaches and presents results as visualisations. Because this approach is unbiased and generalises to various analyses, it can help scientists identify unexpected biological processes. The associated visualisations provide scientists with high-level views of their discoveries thus enabling the identification of new patterns in data.
