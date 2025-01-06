# Immunogenicity of autologous and allogeneic human primary cholangiocyte organoids

#### ABSTRACT

Primary human cells cultured in 3D organoid format have great promise as potential regenerative cellular therapies, but their immunogenicity has not yet been fully characterized. In this study, we use *in vitro* co-cultures and *in vivo* humanized mouse experimental models to examine the human immune response to autologous and allogeneic primary cholangiocyte organoids (PCOs). Our data demonstrate that PCOs upregulate the expression of HLA-I and HLA-II in inflammatory conditions. The immune response to allogeneic PCOs is driven by both HLA-I and HLA-II and is substantially ameliorated by donor-recipient HLA matching. Autologous PCOs induce a low-level immune infiltration into the graft site, while allogeneic cells display evolving stages of immune rejection *in vivo*. Our findings have important implications for the design and clinical translation of autologous and allogeneic organoid cellular therapies.

#### GENERAL INFORMATION

Title of Dataset: Immunogenicity of autologous and allogeneic human primary cholangiocyte organoids

*   Author Information
    A. Principal Investigator Contact Information
    Name: Kourosh Saeb-Parsy
    Institution: Department of Surgery, University of Cambridge
    Address: Box 202. Level 9. Addenbrooke's Hospital · Hills Road *Cambridge* CB2 0QQ

<!---->

*   Associate or Co-investigator Contact Information
    Name: Sandra Petrus-Reurer
    Institution: Department of Surgery, University of Cambridge
    Address: Box 202. Level 9. Addenbrooke's Hospital · Hills Road *Cambridge* CB2 0QQ

Date of data collection (single date, range, approximate date): 2022-2023

Information about funding sources that supported the collection of the data: (MR/S020934/1, Medical Research Council (MRC) UK Regenerative Medicine Platform, G116517, MRC Confidence in Concept, and ERC: 741707, European Research Council Grant New-Chol

#### SHARING/ACCESS INFORMATION

Licenses/restrictions placed on the data: CC0 1.0 Universal (CC0 1.0) Public Domain

Links to publications that cite or use the data:

*   Petrus-Reurer, Sandra & Tysoe, Olivia & Lei, Winnie & Mairesse, Maelle & Tan, Thomas & Rehakova, Sylvia & Mahbubani, Krishnaa & Jones, Julia & Brodie, Cara & Han, Namshik & Betts, Catherine & Vallier, Ludovic & Saeb-Parsy, Kourosh. (2024). Immunogenicity of autologous and allogeneic human primary cholangiocyte organoids. 10.1101/2024.01.11.574744.

Links to other publicly accessible locations of the data: None

Links/relationships to ancillary data sets: None

Was data derived from another source? No

Recommended citation for this dataset:

*   Petrus-Reurer, Sandra & Tysoe, Olivia & Lei, Winnie & Mairesse, Maelle & Tan, Thomas & Rehakova, Sylvia & Mahbubani, Krishnaa & Jones, Julia & Brodie, Cara & Han, Namshik & Betts, Catherine & Vallier, Ludovic & Saeb-Parsy, Kourosh. (2024). Immunogenicity of autologous and allogeneic human primary cholangiocyte organoids. 10.1101/2024.01.11.574744.

#### DATA & FILE OVERVIEW

This is a freeform section for you to describe how the data are structured and how a potential consumer might use them. Be as descriptive as necessary. Keep in mind that users of your data might be new to the field and unfamiliar with common terminology, metrics, etc.

File List:

*   Annotation.csv
*   Matrix.csv
*   Metadata.csv

Relationship between files, if important:

*   The samplename in Metadata.csv corresponds to the column in Matrix.csv
*   The in Metadata.csv corresponds to the in Annotation.csv

Additional related data collected that was not included in the current data package: None

\#########################################################################

DATA-SPECIFIC INFORMATION FOR: Annotation.csv

Comma-delimited spreadsheet containing gene target properties information.

Number of variables: 13

Number of cases/rows: 18676

Variable List:

*   TargetName: Name given to target that may include the gene name; target level name may not be unique whereas probe level name is unique; in the case of multiple gene targets only one gene name is given
*   HUGOSymbol: Comma-delimited list of name of gene(s) with >=95% identity over the length of probe; human gene names follow HUGO gene nomenclature;
*   TargetGroup: Target group as defined by the DSPDA software during analysis; multiple groups of targets can be user-defined; “All Targets” is a default group containing all targets in an assay
*   AnalyteType: AnalyteType	Type of biological target, either RNA or Protein
*   CodeClass: Class of target used for analysis; value is either Control, Negative, or Endogenous
*   ProbePool: Integer value that identifies a single pool of probes; in the case multiple assays are used together, there would be more than one integer value in this list
*   MinCount: Minimum count observed for the target from all segments
*   MaxCount: Maximum count observed for the target from all segments
*   MedianCount: Median count measured for the target from all segments
*   GeomeanCount: Geometric mean of all counts for the target from all segments
*   NumberOfProbesIncluded: Number of probes included in the target in analysis after QC
*   NumberOfProbesTotal: Number of probes included in the target prior to QC
*   GeneID: The field identifies the one NCBI gene ID from the "SystematicName" column recommended for use in pathway analysis

Missing data codes: NA (not applicable)

Specialized formats or other abbreviations used: NA

\#########################################################################

DATA-SPECIFIC INFORMATION FOR: Matrix.csv

Comma-delimited spreadsheet containing Q3 (third quantile) normalized gene-counts matrix. Samples are specified in columns and genes (Variables) are in rows.

Number of variables: 14766

Number of cases/rows: 91

Variable List:

*   ID_REF: TargetName

Missing data codes: NA

Specialized formats or other abbreviations used: NA

\#########################################################################

DATA-SPECIFIC INFORMATION FOR: Metadata.csv

Comma-delimited spreadsheet containing the meta data describing the FFPE samples from mouse model engrafted with human cholangiocyte organoids under kidney capsule by sample name.

Number of variables: 22

Number of cases/rows: 91

Variable List:

*   Sample.name: sample name corresponding to the column names in matrix.

*   source.name: Type of cells analysed in the sample; value is either KRT+ cells or CD45+ cells

*   organism: The organism which the samples were derived

*   Tag: Type of humanisation and HLA class matching; value is either Non_Humanised, Full_Mismatch_Control, Full_Mismatch, Autologous, Partial_Mismatch, Partial_Mismatch_Control, or Autologous_Control

*   ROI.number: Numeric identifier for ROI; all segments within one ROI will have the same ROI number

*   AOISurfaceArea: Segment surface area, in pixels after conversion of scan in mm

*   AOINucleiCount: AOINucleiCount	Segment nuclei count derived using the following algorithm in DSPDA v2.4 or earlier.

*   ROICoordinateX: x-coordinate of the ROI center on the Raw Channel Image exported from DSPDA, x starts on the left with 0 and extends right, in pixels

*   ROICoordinateY: y-coordinate of the ROI center on the Raw Channel Image, y starts at the top with 0 and extends down, in pixels

*   RawReads: Number of read pairs initially inputted into the GeoMx NGS Pipeline

*   AlignedReads: Number of reads remaining after alignment to the barcode whitelist

*   DeduplicatedReads: Number of reads remaining after removal of PCR duplicates (i.e. unique UMIs)

*   TrimmedReads: Number of read pairs remaining after quality and adapter trimming

*   StitchedReads: Number of reads remaining after stitching overlapping sequences of Read 1 and Read 2

*   SequencingSaturation: Sequencing saturation is related to sequencing depth and dependent on the given library complexity and reads sequenced; Proportion of UMIs in library sequenced more than once, sequencing saturation = (1 - deduplicated reads / aligned reads)

*   ScanWidth: Width of the largest rendered scan image, in pixels after conversion of scan width from mm; used to calculate the ROI center of an exported image using the following equation (result in pixels with origin (0,0) at the bottom left):  Export X coordinate = (ROICoordinateX -ScanOffsetX) * (Export width/ScanWidth)

*   ScanHeight: Height of the largest rendered scan image, in pixels after conversion of scan height from mm; used to calculate the ROI center of an exported image using the following equation (result in pixels with origin (0,0) at the bottom left):  Export Y coordinate = Export height - ((ROICoordinateY -ScanOffsetY) * (Export height/ScanHeight))

*   ScanOffsetX: x offset of the start of the rendered scan image relative to the raw image, in pixels; used to calculate the ROI center of an exported image  using the following equation (result in pixels with origin (0,0) at the bottom left):  Export X coordinate = (ROICoordinateX -ScanOffsetX) * (Export width/ScanWidth)

*   ScanOffsetY: y offset of the start of the rendered scan image relative to the raw image, in pixels; used to calculate the ROI center of an exported image using the following equation (result in pixels with origin (0,0) at the bottom left):  Export Y coordinate = Export height - ((ROICoordinateY -ScanOffsetY) * (Export height/ScanHeight))

*   LOQ: LOQ is equivalent to the geomean of negative probes in a given segment plus a user-defined number of standard deviations [geomean(neg probes)*geoSD(neg probes)^X, where X is a user-defined value (default = 2)]. The default value of 2 should be used if a slightly higher false positive rate (<5%) is acceptable in exchange for higher sensitivity. Consider changing the value to 2.5 to minimize false positive calls (~1%), although this may decrease sensitivity slightly. The LOQ threshold can be used downstream to filter out targets that are not detected in at least a certain percentage of segments or when making binary detected/not detected calls.

*   description: Description of the sample.

*   platform: The platform accession number in GEO.

Missing data codes: NA (not applicable)

Specialized formats or other abbreviations used: NA

#### CODE/SOFTWARE

*   BHOT_Analysis.Rmd: Analysis of immunogenicity associated pathways enrichment from differential expression results BHOT data ([https://onlinelibrary.wiley.com/doi/full/10.1111/ajt.16059).](https://onlinelibrary.wiley.com/doi/full/10.1111/ajt.16059\).)
*   CD45_DE_Analysis.html: Analysis of differentially expressed genes between humanised and non-humanised samples CD45+ cells.
*   CellDecon_Analysis.Rmd: Analysis to estimate cell abundance in CD45+ spatial gene expression data.
*   KRT_DE_Analysis.Rmd: Analysis of differentially expressed genes between humanised and non-humanised samples cholangiocytes.

