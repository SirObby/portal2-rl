#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "demo.h"
#include "demo_info.h"

void go_user_cmd(const Demo *d) {}

int main(int argc, char **argv)
{
    if (argc == 1)
    {
        printf("nah");
        exit(-1);
    }

    int parse_level = -1;
    bool debug_mode = false;

    for (size_t i = 1; i < argc; i++)
    {
        char *input_file = argv[i];
        printf("%s\n", argv[i]);

        Demo *demo = new_demo(input_file);
        int result = demo_parse(demo, parse_level, debug_mode);

        printf("%s, %s, %s\n", (demo->game == PORTAL_2) ? "PORTAL 2" : "OTHER", demo->file_name, demo->header.client_name);

        if (result == MEASURED_ERROR)
        {
            printf("Could not read?");
            continue;
        }

        for (size_t i = 0; i < demo->messages.size; i++)
        {
            const DemoMessage *msg = &demo->messages.data[i];
            int tick = msg->tick;

            int stop = demo_info.msg_settings->enum_ids[Stop_MSG];
            int console_cmd = demo_info.msg_settings->enum_ids[ConsoleCmd_MSG];
            int user_cmd = demo_info.msg_settings->enum_ids[UserCmd_MSG];

            if (tick > 0)
            {
                int type = msg->type;
                if (type == stop)
                {
                    break;
                }
                if (type == console_cmd)
                {
                    char *command = (char *)msg->data.ConsoleCmd_message.data;
                    //    fprintf(fp, "_y_spt_afterframes %d \"%s;\";\n", tick, command);
                    printf("%dC, %s\n", tick, command);
                }
                else if (type == user_cmd)
                {
                    const UserCmdInfo *cmd = &msg->data.UserCmd_message.data;
                    //    fprintf(fp, "_y_spt_afterframes %d \"_y_spt_setangles %.8f %.8f;\";\n", tick, cmd->view_angles_x, cmd->view_angles_y);
                    printf("%d, %d %.8f, %.8f, %d\n", tick, cmd->forward_move, cmd->view_angles_x, cmd->view_angles_y, cmd->buttons);
                }
            }
        }
    }
}