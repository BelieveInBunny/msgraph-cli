# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_notes_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_notes.vendored_sdks.notes import Notes
    return get_mgmt_service_client(cli_ctx,
                                   Notes,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups


def cf_group_onenote(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote


def cf_group_onenote_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_notebooks


def cf_group_onenote_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_notebooks_section_groups


def cf_group_onenote_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_notebooks_section_groups_sections


def cf_group_onenote_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_notebooks_section_groups_sections_pages


def cf_group_onenote_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_notebooks_sections


def cf_group_onenote_notebook_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_notebooks_sections_pages


def cf_group_onenote_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_notebooks_sections_parent_section_group


def cf_group_onenote_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages


def cf_group_onenote_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_notebook


def cf_group_onenote_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_notebook_section_groups


def cf_group_onenote_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_notebook_section_groups_sections


def cf_group_onenote_page_parent_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_notebook_sections


def cf_group_onenote_page_parent_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_notebook_sections_parent_section_group


def cf_group_onenote_page_parent_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_section


def cf_group_onenote_page_parent_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_section_parent_notebook


def cf_group_onenote_page_parent_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_section_parent_notebook_section_groups


def cf_group_onenote_page_parent_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_section_parent_section_group


def cf_group_onenote_page_parent_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_pages_parent_section_parent_section_group_parent_notebook


def cf_group_onenote_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups


def cf_group_onenote_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups_parent_notebook


def cf_group_onenote_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups_parent_notebook_sections


def cf_group_onenote_section_group_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups_parent_notebook_sections_pages


def cf_group_onenote_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups_sections


def cf_group_onenote_section_group_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups_sections_pages


def cf_group_onenote_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups_sections_pages_parent_notebook


def cf_group_onenote_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_section_groups_sections_parent_notebook


def cf_group_onenote_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections


def cf_group_onenote_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections_pages


def cf_group_onenote_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections_pages_parent_notebook


def cf_group_onenote_section_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections_pages_parent_notebook_section_groups


def cf_group_onenote_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections_parent_notebook


def cf_group_onenote_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections_parent_notebook_section_groups


def cf_group_onenote_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections_parent_section_group


def cf_group_onenote_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).groups_onenote_sections_parent_section_group_parent_notebook


def cf_site(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites


def cf_site_onenote(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote


def cf_site_onenote_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_notebooks


def cf_site_onenote_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_notebooks_section_groups


def cf_site_onenote_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_notebooks_section_groups_sections


def cf_site_onenote_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_notebooks_section_groups_sections_pages


def cf_site_onenote_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_notebooks_sections


def cf_site_onenote_notebook_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_notebooks_sections_pages


def cf_site_onenote_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_notebooks_sections_parent_section_group


def cf_site_onenote_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages


def cf_site_onenote_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_notebook


def cf_site_onenote_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_notebook_section_groups


def cf_site_onenote_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_notebook_section_groups_sections


def cf_site_onenote_page_parent_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_notebook_sections


def cf_site_onenote_page_parent_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_notebook_sections_parent_section_group


def cf_site_onenote_page_parent_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_section


def cf_site_onenote_page_parent_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_section_parent_notebook


def cf_site_onenote_page_parent_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_section_parent_notebook_section_groups


def cf_site_onenote_page_parent_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_section_parent_section_group


def cf_site_onenote_page_parent_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_pages_parent_section_parent_section_group_parent_notebook


def cf_site_onenote_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups


def cf_site_onenote_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups_parent_notebook


def cf_site_onenote_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups_parent_notebook_sections


def cf_site_onenote_section_group_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups_parent_notebook_sections_pages


def cf_site_onenote_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups_sections


def cf_site_onenote_section_group_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups_sections_pages


def cf_site_onenote_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups_sections_pages_parent_notebook


def cf_site_onenote_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_section_groups_sections_parent_notebook


def cf_site_onenote_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections


def cf_site_onenote_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections_pages


def cf_site_onenote_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections_pages_parent_notebook


def cf_site_onenote_section_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections_pages_parent_notebook_section_groups


def cf_site_onenote_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections_parent_notebook


def cf_site_onenote_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections_parent_notebook_section_groups


def cf_site_onenote_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections_parent_section_group


def cf_site_onenote_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).sites_onenote_sections_parent_section_group_parent_notebook


def cf_user(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users


def cf_user_onenote(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote


def cf_user_onenote_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_notebooks


def cf_user_onenote_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_notebooks_section_groups


def cf_user_onenote_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_notebooks_section_groups_sections


def cf_user_onenote_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_notebooks_section_groups_sections_pages


def cf_user_onenote_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_notebooks_sections


def cf_user_onenote_notebook_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_notebooks_sections_pages


def cf_user_onenote_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_notebooks_sections_parent_section_group


def cf_user_onenote_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages


def cf_user_onenote_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_notebook


def cf_user_onenote_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_notebook_section_groups


def cf_user_onenote_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_notebook_section_groups_sections


def cf_user_onenote_page_parent_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_notebook_sections


def cf_user_onenote_page_parent_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_notebook_sections_parent_section_group


def cf_user_onenote_page_parent_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_section


def cf_user_onenote_page_parent_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_section_parent_notebook


def cf_user_onenote_page_parent_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_section_parent_notebook_section_groups


def cf_user_onenote_page_parent_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_section_parent_section_group


def cf_user_onenote_page_parent_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_pages_parent_section_parent_section_group_parent_notebook


def cf_user_onenote_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups


def cf_user_onenote_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups_parent_notebook


def cf_user_onenote_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups_parent_notebook_sections


def cf_user_onenote_section_group_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups_parent_notebook_sections_pages


def cf_user_onenote_section_group_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups_sections


def cf_user_onenote_section_group_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups_sections_pages


def cf_user_onenote_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups_sections_pages_parent_notebook


def cf_user_onenote_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_section_groups_sections_parent_notebook


def cf_user_onenote_section(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections


def cf_user_onenote_section_page(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections_pages


def cf_user_onenote_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections_pages_parent_notebook


def cf_user_onenote_section_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections_pages_parent_notebook_section_groups


def cf_user_onenote_section_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections_parent_notebook


def cf_user_onenote_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections_parent_notebook_section_groups


def cf_user_onenote_section_parent_section_group(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections_parent_section_group


def cf_user_onenote_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_cl(cli_ctx).users_onenote_sections_parent_section_group_parent_notebook
