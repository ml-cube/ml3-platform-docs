# User Roles

The Company owner can create new Users assigning to them a Role.
The Role defines a set of actions a User has inside the application.
Each User has associated a *company role* and one or more *project roles*.


<figure markdown>
  ![Image title](../imgs/user roles.png){ width="500" }
  <figcaption>User Roles in ML cube Platform.</figcaption>
</figure>

The following tables shows the User roles:

## Company Permissions
{{ read_csv('../tables/rbac_company.csv') }}

## Project Permissions
{{ read_csv('../tables/rbac_project.csv') }}

