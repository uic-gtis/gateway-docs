# Admin web files

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This document describes the HTTP API exposed by `AdminWebFilesController`, deployed at `http://travelmidwest.com/lmiga/admin/webfiles`. **Admin-level privileges** are required to access these endpoints.

## Authentication

- All requests must include credentials or tokens with admin-level access.
- Unauthorized requests will receive HTTP **401** or **403** responses.

## Base URL

```
http://travelmidwest.com/lmiga/admin/webfiles`
```

## Endpoints

### Get Root Directory

- **Method**: GET
- **URL**: `/`
- **Description**: Returns the root `WebDirectory` metadata, including its immediate children.
- **Response**: JSON `WebFileDto` with `type = "directory"` and a `children` array.

```json
{ 
  "id": 1, 
  "name": "", 
  "path": "", 
  "type": 
  "directory", 
  "creationDate": "2025-04-01T12:00:00Z", 
  "modificationDate": "2025-04-01T12:00:00Z", 
  "owner": "admin", 
  "children": [ /* ... */ ] 
}
```

### Get File or Directory by Path

- **Method**: GET
- **URL**: `/{filePath}`
- **Path Variable**: `filePath` — slash-delimited path (e.g. `images/logo.png` or `docs/manual`).
- **Content Negotiation**:
  - `Accept: application/json` → Returns metadata (`WebFileDto`).
  - `Accept: application/octet-stream` or query `?download=true` → Returns raw file bytes.
- **Responses**:
  - **200**: Success, returns JSON or binary body.
  - **404**: File/directory not found.

### Alternative GET by Request Parameter

- **Method**: GET
- **URL**: `/path?path={filePath}`
- Behaves identically to endpoint #2.

### Create File or Directory

- **Method**: POST
- **URL**: `/{filePath}`
- **Query Params**:
  - `isDirectory` (boolean, default `false`) — set to `true` to create a directory.
- **Request Parts**:
  - `file` (multipart, required if `isDirectory=false`) — file contents.
  - `metadata` (optional JSON) — `FileMetadataDto` with `altText` field.
- **Responses**:
  - **200**: Success, returns created `WebFileDto`.
  - **400**: Invalid path, missing file, or parent not found.

### Update File

- **Method**: PUT
- **URL**: `/{filePath}`
- **Path Variable**: `filePath` — existing file to update.
- **Request Parts**:
  - `file` (multipart, required) — new file contents.
  - `metadata` (optional JSON) — updated `altText` for images.
- **Responses**:
  - **200**: Success, returns updated `WebFileDto`.
  - **400**: Trying to update a directory or invalid path.

### Rename or Move File/Directory

- **Method**: PATCH
- **URL**: `/{filePath}`
- **Path Variable**: `filePath` — current path of the item.
- **Request Body** (JSON `RenameDto`):
```
{ "newName": "renamed.txt", /* required */ "newParentPath": "images" /* optional; omit to stay in current directory */ }
```

- **Behavior**:
  - Files use internal `moveTo(newDirectory, newName)`.
  - Directories are removed from their old parent, renamed, then added to the new parent.
- **Responses**:
  - **200**: Success, returns renamed `WebFileDto`.
  - **400**: Invalid name, parent not a directory, or naming conflict.
  - **404**: Item not found.

### Delete File or Directory

- **Method**: DELETE
- **URL**: `/{filePath}`
- **Path Variable**: `filePath` — item to delete.
- **Responses**:
  - **200**: Success, returns `true`.
  - **400**: Cannot delete root or invalid path.
  - **404**: Item not found.

## Data Transfer Objects

### WebFileDto

|  |  |  |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| id | Long | Database identifier |
| name | String | Filename or directory name |
| path | String | Full path (no leading slash) |
| type | String | `"file"` or `"directory" |
| creationDate | Date | Timestamp of creation |
| modificationDate | Date | Timestamp of last modification |
| owner | String | Owner username or identifier |
| altText | String | *[files only]* alt text for images |
| children | List | *[dirs only]* child items |

### FileMetadataDto

|  |  |  |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| altText | String | Alternate text for file display. |

### RenameDto

|  |  |  |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| newName | String | New name for the file or directory (req) |
| newParentPath | String | Path of target directory (optional) |

## Usage Examples

### Fetch Directory Metadata in React

```javascript
fetch('/lmiga/admin/webfiles', {
  headers: { 'Accept': 'application/json' }
})
  .then(res => res.json())
  .then(data => console.log(data));
```

### Download a File

```javascript
fetch('/lmiga/admin/webfiles/docs/report.pdf?download=true', {
  headers: { 'Accept': 'application/octet-stream' }
})
  .then(res => res.blob())
  .then(blob => { /* save or display */ });
```

### Create a Sub-directory

```javascript
const form = new FormData();
form.append('isDirectory', 'true');
fetch('/lmiga/admin/webfiles/images/newFolder', {
  method: 'POST',
  body: form,
});
```

### Rename a File

```javascript
fetch('/lmiga/admin/webfiles/images/oldName.jpg', {
  method: 'PATCH',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ newName: 'newName.jpg' })
});
```

## Error Handling

- **400 Bad Request**: Invalid input, naming conflicts, or operation not allowed.
- **401 Unauthorized** / **403 Forbidden**: Missing or insufficient privileges.
- **404 Not Found**: Specified file or directory does not exist.

## Public URLs

Note that the public URL for the files managed by this admin controller can be obtained by removing the /admin/webfiles portion of the file's URL.

Example:

| Administration "GET", "PUT", "PATCH", and "DELETE" URL for File | Public "GET" URL for File |
| --- | --- |
| https://travelmidwest.com/lmiga**/admin/webfiles**/webfile/images/DuPageCty.JPG | https://travelmidwest.com/lmiga/webfile/images/DuPageCty.JPG |
