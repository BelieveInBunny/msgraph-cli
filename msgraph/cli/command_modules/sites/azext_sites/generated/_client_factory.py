# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_sites_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_sites.vendored_sdks.sites import Sites
    return get_mgmt_service_client(cli_ctx,
                                   Sites,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_group(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).groups


def cf_sitessite(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitessite


def cf_site(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites


def cf_sitescontenttype(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitescontenttypes


def cf_siteslist(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).siteslists


def cf_siteslistscontenttype(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).siteslistscontenttypes


def cf_siteslistsitem(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).siteslistsitems


def cf_siteslistsitemsversion(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).siteslistsitemsversions


def cf_sitesonenotenotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebooks


def cf_sitesonenotenotebookssectiongroupsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectiongroupsparentnotebook


def cf_sitesonenotenotebookssectiongroupssection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectiongroupssections


def cf_sitesonenotenotebookssectiongroupssectionspage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectiongroupssectionspages


def cf_sitesonenotenotebookssectiongroupssectionspagesparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectiongroupssectionspagesparentnotebook


def cf_sitesonenotenotebookssectiongroupssectionspagesparentsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectiongroupssectionspagesparentsection


def cf_sitesonenotenotebookssectiongroupssectionsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectiongroupssectionsparentnotebook


def cf_sitesonenotenotebookssection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssections


def cf_sitesonenotenotebookssectionspage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectionspages


def cf_sitesonenotenotebookssectionspagesparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectionspagesparentnotebook


def cf_sitesonenotenotebookssectionspagesparentsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectionspagesparentsection


def cf_sitesonenotenotebookssectionsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectionsparentnotebook


def cf_sitesonenotenotebookssectionsparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectionsparentsectiongroupparentnotebook


def cf_sitesonenotenotebookssectionsparentsectiongroupsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotenotebookssectionsparentsectiongroupsections


def cf_sitesonenotepage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepages


def cf_sitesonenotepagesparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebook


def cf_sitesonenotepagesparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectiongroupsparentnotebook


def cf_sitesonenotepagesparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectiongroupssections


def cf_sitesonenotepagesparentnotebooksectiongroupssectionspage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectiongroupssectionspages


def cf_sitesonenotepagesparentnotebooksectiongroupssectionsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectiongroupssectionsparentnotebook


def cf_sitesonenotepagesparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksections


def cf_sitesonenotepagesparentnotebooksectionspage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectionspages


def cf_sitesonenotepagesparentnotebooksectionsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectionsparentnotebook


def cf_sitesonenotepagesparentnotebooksectionsparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectionsparentsectiongroupparentnotebook


def cf_sitesonenotepagesparentnotebooksectionsparentsectiongroupsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentnotebooksectionsparentsectiongroupsections


def cf_sitesonenotepagesparentsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsection


def cf_sitesonenotepagesparentsectionpage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionpages


def cf_sitesonenotepagesparentsectionparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionparentnotebook


def cf_sitesonenotepagesparentsectionparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionparentnotebooksectiongroupsparentnotebook


def cf_sitesonenotepagesparentsectionparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionparentnotebooksectiongroupssections


def cf_sitesonenotepagesparentsectionparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionparentnotebooksections


def cf_sitesonenotepagesparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionparentsectiongroupparentnotebook


def cf_sitesonenotepagesparentsectiongroupparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionparentsectiongroupparentnotebooksections


def cf_sitesonenotepagesparentsectiongroupsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotepagesparentsectionparentsectiongroupsections


def cf_sitesonenotesectiongroupsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupsparentnotebook


def cf_sitesonenotesectiongroupsparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupsparentnotebooksections


def cf_sitesonenotesectiongroupsparentnotebooksectionspage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupsparentnotebooksectionspages


def cf_sitesonenotesectiongroupsparentnotebooksectionspagesparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupsparentnotebooksectionspagesparentnotebook


def cf_sitesonenotesectiongroupsparentnotebooksectionspagesparentsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupsparentnotebooksectionspagesparentsection


def cf_sitesonenotesectiongroupsparentnotebooksectionsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupsparentnotebooksectionsparentnotebook


def cf_sitesonenotesectiongroupssection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupssections


def cf_sitesonenotesectiongroupssectionspage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupssectionspages


def cf_sitesonenotesectiongroupssectionspagesparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupssectionspagesparentnotebook


def cf_sitesonenotesectiongroupssectionspagesparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupssectionspagesparentnotebooksections


def cf_sitesonenotesectiongroupssectionspagesparentsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupssectionspagesparentsection


def cf_sitesonenotesectiongroupssectionsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupssectionsparentnotebook


def cf_sitesonenotesectiongroupssectionsparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectiongroupssectionsparentnotebooksections


def cf_sitesonenotesection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesections


def cf_sitesonenotesectionspage(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionspages


def cf_sitesonenotesectionspagesparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionspagesparentnotebook


def cf_sitesonenotesectionspagesparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionspagesparentnotebooksectiongroupsparentnotebook


def cf_sitesonenotesectionspagesparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionspagesparentnotebooksectiongroupssections


def cf_sitesonenotesectionspagesparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionspagesparentnotebooksections


def cf_sitesonenotesectionspagesparentsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionspagesparentsection


def cf_sitesonenotesectionsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionsparentnotebook


def cf_sitesonenotesectionsparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionsparentnotebooksectiongroupsparentnotebook


def cf_sitesonenotesectionsparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionsparentnotebooksectiongroupssections


def cf_sitesonenotesectionsparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionsparentnotebooksections


def cf_sitesonenotesectionsparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionsparentsectiongroupparentnotebook


def cf_sitesonenotesectionsparentsectiongroupparentnotebooksection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionsparentsectiongroupparentnotebooksections


def cf_sitesonenotesectionsparentsectiongroupsection(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sitesonenotesectionsparentsectiongroupsections


def cf_user(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).users
