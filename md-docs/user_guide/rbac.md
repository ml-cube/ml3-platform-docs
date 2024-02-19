# User Roles

The Company owner can create new Users assigning to them a Role.
The Role defines a set of actions a User has inside the application.
Each User has associated a *company role* and one or more *project roles*.

!!! tip "Delta Energy inc"

    Delta Energy has one dedicatd AI Team to each Task. Hence, they assigned specific Project Administrator Role to each Team leader; while the other Data Scientists have the Project Edit Role for the project they are working on.

<figure markdown>
  ![Image title](../imgs/user roles.png){ width="500" }
  <figcaption>User Roles in ML cube Platform.</figcaption>
</figure>

The following tables shows the User roles:

## Company Permissions
{{ read_csv('../tables/rbac_company.csv') }}

## Project Permissions
{{ read_csv('../tables/rbac_project.csv') }}

