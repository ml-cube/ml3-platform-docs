# Exports

Exports package task data and analysis results into portable files that can be
used outside ML cube Platform. Each export covers an inclusive range of [data
batches] and one or more content bundles.

Open a task and select **Exports** from the task menu. The page is available
when the Export feature is enabled for the platform and the company
subscription. Users with read access to the project can view exports and obtain
download links; creating an export requires permission to work on the project.

<!-- SCREENSHOT PLACEHOLDER: Exports page
Capture the complete Exports page for a task that has several exports. Include
the Create new export button, filters, and table rows with a useful mix of
statuses (preferably Completed, Running, and Failed). Do not expose real signed
download URLs or sensitive task data.

Replace this comment with:
<figure markdown>
  ![Exports page](../../imgs/exports/exports-page.png)
  <figcaption>Exports created for a task.</figcaption>
</figure>
-->

## Bundles

A bundle is a family of related content, not necessarily a single file. The
bundles offered in the creation dialog depend on the task type, its data
structure, the enabled modules, and the company subscription.

| Bundle | Contents and availability |
| --- | --- |
| **Data** | Task samples from the selected batches in Parquet format. For image tasks, the bundle can also contain ZIP archives of images and novelty heatmaps when they are available. |
| **Dynamic clustering** | Available for tasks other than time-series tasks. It can contain [Dynamic clustering] results, transition results, and active microcluster results in Parquet format. Only results available for the selected range are included. |
| **RAG evaluation reports** | Available for RAG tasks when [RAG evaluation] is enabled. It contains evaluation metrics from reports covered by the selected batches in Parquet format. |
| **LLM security reports** | Available for RAG tasks when [LLM Security] is enabled. It contains the available security report results for the selected range in Parquet format. |
| **Topic modeling reports** | Available for text tasks when [Topic Analysis] is enabled. It contains the available topic modeling results for the selected range in Parquet format. |

Selecting a bundle does not guarantee that every possible file in that bundle
will be produced. Files are generated only for data or analysis results that
exist in the selected batch range. An export can therefore complete with fewer
files than expected, or with no downloadable files.

## Create an export

1. Open the task and select **Exports**.
2. Select **Create new export**.
3. Enter the **Starting batch index** and **Ending batch index**. Both ends of
   the range are included.
4. Select one or more **Bundles**.
5. Select **Create**.

When task batches are available, the dialog initially selects the full range
from batch `0` through the highest available batch index. Both indices must be
non-negative whole numbers, neither can exceed the maximum shown by the dialog,
and the ending index cannot be lower than the starting index.

If the task has no data batches, the dialog reports that there is no data to
export and the **Create** button remains unavailable.

<!-- SCREENSHOT PLACEHOLDER: Create new export dialog
Capture the Create new export dialog after opening the Bundles selector. Show a
valid batch range and all bundle choices available for a task with multiple
enabled modules. Avoid using a task whose name or data is sensitive.

Replace this comment with:
<figure markdown>
  ![Create new export dialog](../../imgs/exports/create-export.png)
  <figcaption>Select an inclusive batch range and the bundles to export.</figcaption>
</figure>
-->

Export generation runs in the background. After the request is accepted, the
new entry appears at the top of the list with the **in queue** status. Select the
refresh icon to load its latest status; the list does not update automatically.

## Export statuses

| Status | Meaning | Available action |
| --- | --- | --- |
| **in queue** | The export request is waiting to be processed. | Refresh the list later. |
| **running** | The selected content is being collected and written. | Refresh the list later. |
| **completed** | Processing finished. | Generate download links before the expiration date. |
| **failed** | Processing stopped because of an error. | Select the error-details icon to read the failure message. |
| **expired** | The export has passed its retention period. | Create a new export if the files are still needed. |

Each export has an **Expiration date**. Exported files are retained for three
days from the export's creation time. They cannot be downloaded after that
date, even if the row still shows that processing completed successfully.

!!! note
    A failed export cannot be resumed from the list. Review its error details,
    correct the underlying data or module issue when possible, and create a new
    export.

## Download exported files

Download links can be generated only for a completed export that has not
expired.

1. Find the completed export in the list.
2. Select the link icon in the **Status** column.
3. In the **Download links** dialog, expand or collapse each bundle group as
   needed.
4. Select the copy icon beside a file and open the copied URL to download that
   file.

The dialog identifies every file by its bundle name and file type. Select
**Download JSON** to save all the displayed links and their metadata in a file
named `export-<export-id>-links.json`. This JSON file is a link manifest; it does
not contain the exported data itself.

<!-- SCREENSHOT PLACEHOLDER: Download links dialog
Capture the Download links dialog for a completed export with at least two
expanded bundle groups and multiple files. Keep the Download JSON button and
copy-link actions visible, but blur or replace the signed URL values.

Replace this comment with:
<figure markdown>
  ![Export download links](../../imgs/exports/download-links.png)
  <figcaption>Download links grouped by bundle.</figcaption>
</figure>
-->

!!! warning
    Download links provide direct access to exported task content. Treat them as
    sensitive, share them only with authorized recipients, and do not place them
    in public tickets, chat rooms, or source repositories. Generated links may
    stop working before the export itself expires; generate a fresh set from the
    completed export when needed.

## Find an export

Exports are listed from newest to oldest. Use the filters to narrow the history:

- **Creation date** includes exports created on any day in the selected date
  range.
- **Starting batch index** includes exports whose starting index is equal to or
  greater than the entered value.
- **Ending batch index** includes exports whose ending index is equal to or
  lower than the entered value.
- **Active exports only** is selected by default and hides exports whose
  expiration date has passed. Clear it to include the full export history.

When both batch filters are set, the results are exports whose complete batch
range fits within those boundaries. Select **Apply Filters** to update the list
or **Reset** to restore the defaults. Use the paginator to change pages or the
number of rows shown.

## Troubleshooting

- **Exports is missing from the task menu**: confirm that the Export feature is
  enabled for the platform and included in the company subscription.
- **No bundles are available**: bundle availability depends on the task type,
  data structure, enabled modules, and subscription. The Data bundle is offered
  when exporting is available.
- **Create is unavailable**: confirm that the task has at least one data batch,
  both indices are valid, and at least one bundle is selected. Also confirm that
  you have permission to work on the project.
- **The new export remains in queue or running**: wait for processing to finish,
  then select the refresh icon to retrieve the latest status.
- **An export failed**: select its error-details icon for more information, then
  create a new export after resolving the cause.
- **A completed export has no links**: none of the requested data or analysis
  artifacts were available in the selected batch range. Try another range or
  confirm that the relevant module has produced results.
- **A download link does not work**: the link itself may have expired. Generate
  the links again while the export is active. If the export's expiration date
  has passed, create a new export.
- **Expected exports are missing**: clear **Active exports only**, reset the
  other filters, and check additional result pages.

[Data batches]: ../data.md#data-batch
[Dynamic clustering]: dynamic_clustering.md
[RAG evaluation]: rag_evaluation.md
[LLM Security]: llm_security.md
[Topic Analysis]: topic_modeling.md
