#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "demo.h"
#include "demo_info.h"
#include <json-c/json.h>

#include <dirent.h>

int read_directories(const char *path)
{
    json_object *limits = json_object_from_file("map_limits.json");
    // if (!limits)
    //     return 1;
    // printf("The json file:\n\n%s\n", json_object_to_json_string(limits));

    json_object *out = json_object_new_object();
    // if (!out)
    //     return 1;
    // printf("The json file:\n\n%s\n", json_object_to_json_string(out));

    printf("dir\n");

    DIR *directory = NULL;
    if ((directory = opendir(path)) == NULL)
    {
        fprintf(stderr, "Can't open %s\n", path);
        return EXIT_FAILURE;
    }

    printf("go while\n");

    struct dirent *entry = NULL;
    int j = 0;
    while ((entry = readdir(directory)) != NULL)
    {
        j++;
        char full_name[256] = {0};
        snprintf(full_name, 100, "%s/%s", path, entry->d_name);
        printf("%s\n", full_name);

        if (entry->d_type == DT_DIR)
        {
            printf("'%s' is a directory\n", full_name);
            // Recurse unless the directory is the current or parent directory.
            if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0)
            {
                return read_directories(full_name);
            }
        }
        else
        {

            int parse_level = -1;
            bool debug_mode = false;

            char *input_file = full_name;

            Demo *demo = new_demo(input_file);
            int result = demo_parse(demo, parse_level, debug_mode);

            printf("%d, %s, %s, %s, %s, %s\n", j, (demo->game == PORTAL_2) ? "PORTAL 2" : "OTHER", demo->file_name, demo->header.client_name, demo->header.map_name, demo->header.server_name);

            if (result == MEASURED_ERROR)
            {
                printf("Could not read?");
                continue;
            }

            if (json_object_object_get(json_object_object_get(limits, demo->header.map_name), "name") == NULL) {
                demo_free(demo);
                continue;
            }

            char rn_nm[256] = {0};
            snprintf(rn_nm, 100, "%s_%s_%d", json_object_get_string(json_object_object_get(json_object_object_get(limits, demo->header.map_name), "name")), demo->header.client_name, demo->measured_ticks);
            printf("%s\n", rn_nm);

            printf("%s\n", json_object_get_string(json_object_object_get(json_object_object_get(limits, demo->header.map_name), "name")));
            if (json_object_object_get(out, json_object_get_string(json_object_object_get(json_object_object_get(limits, demo->header.map_name), "name"))) == NULL)
            {
                json_object *jo = json_object_new_object();
                json_object *run_numbers = json_object_new_array();
                json_object *run = json_object_new_object();
                json_object_object_add(run, "time", json_object_new_double((double)demo->header.play_back_time));
                json_object_object_add(run, "name", rn_nm);
                json_object_array_add(run_numbers, run);
                json_object_object_add(jo, "runs", run_numbers);
                json_object_object_add(out, json_object_get_string(json_object_object_get(json_object_object_get(limits, demo->header.map_name), "name")), jo);
            }
            else
            {
                json_object *run_numbers = json_object_object_get(json_object_object_get(out, json_object_get_string(json_object_object_get(json_object_object_get(limits, demo->header.map_name), "name"))), "runs");
                json_object *run = json_object_new_object();
                json_object_object_add(run, "time", json_object_new_double((double)demo->header.play_back_time));
                json_object_object_add(run, "name", rn_nm);
                json_object_array_add(run_numbers, run);
            }

            demo_free(demo);
        }
    }

    json_object_put(limits);
    if (json_object_to_file("map_out.json", out))
        printf("Error: failed to save %s!!\n", "map_out.json");
    else
        printf("%s saved.\n", "map_out.json");

    json_object_put(out);
    closedir(directory);
    return EXIT_SUCCESS;
}

int main(int argc, char **argv)
{
    if (argc == 1)
    {
        printf("nah");
        exit(-1);
    }

    const char *path = argv[1];
    return read_directories(path);

    /*for (size_t i = 1; i < argc; i++)
    {

    }*/
}