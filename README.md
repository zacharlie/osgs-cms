# OSGS-sl

"An OSGS CMS" (yeah, it might be renamed...)

The OSGS-sl project is the "steam locomotive" for the [Open Source Geospatial Stack (OSGS)](https://github.com/kartoza/osgs).

```text
                      (  ) (@@) ( )  (@)  ()    @@    O     @     O     @      O
                 (@@@)
             (    )
          (@@@@)
        (   )
        ++      +------ ____                 ____________________ ____________________
        ||      |+-+ |  |   \@@@@@@@@@@@     |  ___ ___ ___ ___ | |  ___ ___ ___ ___ |
      /---------|| | |  |    \@@@@@@@@@@@@@_ |  |_| |_| |_| |_| | |  |_| |_| |_| |_| |
     + ========  +-+ |  |                  | |__________________| |__________________|
    _|--O========O~\-+  |__________________| |__________________| |__________________|
   //// \_/      \_/       (O)       (O)        (O)        (O)       (O)        (O)
```

In terms of managing and leveraging the myriad of complex and powerful systems and services that are integrated into the OSGS, it's a small connector that turns OSGS users into little engines that can.

## Function

The name osgs-engine may have indicated it has something to do with managing the inner workings and operations of the OSGS.

By contrast, **OSGS-sl** is specifically designed to manage operations facilitating _users_ of OSGS, and is abstracted away from the management of stack components. The [osgs-admin](https://github.com/zacharlie/osgs-admin) is an interface tool designed specifically for managing the OSGS stack elements.

OSGS is a stack of open source software that is fundamentally a collection of tools and services that are designed to make it easier to work with geospatial data. Each service has it's own data management and analysis operations, such as various ways of importing, managing, and extending workflows, services, or analysis tools.

Whilst it is still highly useful and incredibly powerful without OSGS-sl, it requires a certain degree of expertise, and may result in a sub-optimal user experience for complex operations.

Although users with skills in development and/ or managing the OSGS components may continue to utilise those components on their own terms, OSGS-sl is designed to be a first class user experience that includes functionality for simplifying management operations.

## Operations

The OSGS-sl Project aims to provide a platform for various operations, known as "blueprints", which provide enhanced operational functionality, and make the deployment, replication, and extension of end-to-end solutions for the OSGS trivial - even for advanced use cases.

### UX

The user interface is designed as a series of web forms, operational controls, and other interface components. The interfaces perform blueprint actions, but expose this functionality in a way that increases usability.

For example, the articles on the OSGS website utilise simple markdown pages and custom shortcodes for spatial functionality. These might be used from the integrated editor for users experienced with markdown, but an enhanced interface is provided which includes fields for typical metadata and a WYSIWYG Editor. This "What You See Is What You Get" experience is a key to the OSGS-sl project.

An alternative operation would be the provision of a QGIS project and the underlying sample data. The QGIS Server component of the OSGS has specific conventions related to naming of assets and items, whereas it would be possible to provide a file upload interface and use the OSGS-sl component manage such conventions automatically.

These two operations could then be bundled with additional operations, such as thumbnail generation from the map, and integrated into a single publishing step in which users generate an article and map service simultaneously.

### Blueprint Operations

Blueprints provide the ability to load, export, create, and manage OSGS Blueprints, which provide task specific workflows and end-to-end solutions, based on the components and expected configuration structure of the OSGS stack.

Blueprints can be `object` blueprints - which are related to a particular task such as creating a new web page, or `solution blueprints` - which are a specific collection of preconfigured blueprints related to a particular end-to-end solution, such as creating a new field survey project for manhole inspections, which is integrated with a preconfigured dashboard, map service, and analytics API.

# Deploy

Needs db with user, so `flask fab create-admin --username admin --firstname system --lastname administrator --email admin@local.host --password supercalifragilisticexpialidocious` and make sure nobody can access the app.db file.

## Developrmentness

the `requirements.txt.bak` made a nice list of deps but setup.py is more usefuller for proper installation and deployerenerment later.

`pip install -e .[development]`

## i18n

[Docs](https://flask-appbuilder.readthedocs.io/en/latest/i18n.html)

Basically, get strings with `flask fab babel-extract`, translate `./translations/lang/LC_MESSAGES/messages.po` and compile `flask fab babel-compile`.
