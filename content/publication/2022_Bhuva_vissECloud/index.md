---
title: "vissE.cloud: a webserver to visualise higher order molecular phenotypes from enrichment analysis"
authors:
- Ahmed Mohamed
- admin
- Sam Lee
- Ning Liu
- Chin Wee Tan
- Melissa J Davis
date: "2023-05-09"
doi: "https://doi.org/10.1093/nar/gkad337"
author_notes:
  - 'Co-first author'
  - 'Co-first author'

# Schedule page publish date (NOT publication's date).
publishDate: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: "Gene-set analysis (GSA) dominates the functional interpretation of omics data and downstream hypothesis generation. Despite its ability to summarise thousands of measurements into semantically interpretable components, GSA often results in hundreds of significantly enriched gene-sets. However, summarisation and effective visualisation of GSA results to facilitate hypothesis generation is still lacking. While some webservers provide gene-set visualization tools, there is still a need for tools that can effectively summarize and guide exploration of GSA results. To enable versatility, webservers accept gene lists as input, however, none provide end-to-end solutions for emerging data types such as single-cell and spatial omics. Here, we present vissE.Cloud, a webserver for end-to-end gene-set analysis, offering gene-set summarisation and highly interactive visualisation. vissE.Cloud uses algorithms from our earlier R package vissE to summarise GSA results by identifying biological themes. We maintain versatility by allowing analysis of gene lists, as well as, analysis of raw single-cell and spatial omics data, including CosMx and Xenium data, making vissE.Cloud the first webserver to provide end-to-end gene-set analysis of sub-cellular localised spatial data. Structuring the results hierarchically allows swift interactive investigations of results at the gene, gene-set, and clusters level. vissE.Cloud is freely available at https://www.vissE.Cloud."

# Summary. An optional shortened abstract.
summary: vissE.Cloud is a web-server that can help identify, visualise and explore higher-order biological processes from the results of a gene-set enrichment analysis (GSEA). It provides end-to-end analysis of scRNA-seq (10x Chromium) and spatial transcriptomics (10x Visium, 10x Xenium, and NanoString CosMx) datasets.

tags:
- gene-set enrichment analysis
- molecular phenotypes
- networks
- spatial
- single-cell
featured: true

links:
- name: Web tool
  url: https://vissE.cloud
- name: Bioconductor
  url: https://www.bioconductor.org/packages/release/bioc/html/vissE.html
- name: Workshop
  url: https://davislaboratory.github.io/GenesetAnalysisWorkflow/
url_code: 'https://github.com/DavisLaboratory/vissE.cloud'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Schematic of the vissE.cloud workflow'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
