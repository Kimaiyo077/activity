# Form Library

> This is work in progress

## TODOs

Here is the list of Github issues to implement, in rough order:

1. Create a [Service model](https://github.com/hikaya-io/activity/issues/412)
2. Update [Distribution](https://github.com/hikaya-io/activity/issues/419) and [Training](https://github.com/hikaya-io/activity/issues/421) models
3. Adjust fields in [Individual model](https://github.com/hikaya-io/activity/issues/403)
4. Create [Case model](https://github.com/hikaya-io/activity/issues/410)
5. Create [Household model](https://github.com/hikaya-io/activity/issues/409)
6. Create [Attendance models](https://github.com/hikaya-io/activity/issues/422)
7. Create [Inventory model](https://github.com/hikaya-io/activity/issues/418)

## Models

### Current state

Models are gathered inside the directory `models` and [organized as a package](https://docs.djangoproject.com/fr/2.2/topics/db/models/#organizing-models-in-a-package).

If you add models to the folder, just make sure to expose your model in `__init__.py`.

Multi Table Inheritance between model `Service`, and the different kinds of services `Training`, `Distribution`, `Construction`...

`Service` is marked as an abstract class, since a service can't exist without being one, and only one, of the supported service types.

`Case` is a parent model for `Individual` and `Household`?

### Models relationships

Since much refactoring is planned, it is important to keep track of the relationships of the models, especially with models of other applications:

TrainingAttendance:

    ===> workflow/Program
    ===> workflow/ProjectAgreement
    <=== Individual

Individual:

    ===> workflow/SiteProfile
    ===> workflow/Program
    ===> TrainingAttendance
    ===> Distribution

Distribution:

    ===> workflow/Program
    ===> workflow/ProjectAgreement
    ===> workflow/Office
    ===> workflow/Province

> All links to external models are with the `workflow` app

## On Slug fields

Since we are now using UUID for model IDs, we need to associate an expressive slug, deduced from a name, label or description, for more friendly URLs.

## Questions

What would be the common fields between all the currently supported service types (`Training` and `Distribution`), and the potential future ones(`Construction` for example)? Which one of them are required and which are nullable?

- Program
- Site
- Office
- Implementer
- Start and End dates

**About the Case model:**

I feel like `Case`, for now, is just a "parent" to Individual/Household.

We could have a `Recipient` class, or `Receiver`, from which `Individual` and `Household` inherit from, that can satisfy #410. It will:
    - uniquely identify either an Individual or a Household, with no keys duplicated
    - track the services they participated in (NOT exhaustively)

I think the `Case` model would shine if we need to keep a registry related to some generic "events": attending sessions, passing exams/certifications, medical follow-ups...

I don't know if there is other plans for the `Case` model, or this was just the most complicated way to ask if a model could be renamed