#!/usr/bin/env python3

import os
import subprocess
import numpy as np
import shutil
import asyncio
import threading

PORTAL2_DIRECTORY="/home/portal/.steam/steam/steamapps/common/Portal 2"
#PORTAL2_DIRECTORY="/run/media/sir/2tb drive that I own/SteamLibrary/steamapps/common/Portal 2"

async def render_demos():
    for filename in os.listdir("demos/"):
        file = os.path.join("demos/", filename)

        if os.path.isfile(file):
            print(file)
            print(os.path.join(PORTAL2_DIRECTORY, f"portal2/{file}"))
            #shutil.copy2(file,os.path.join(PORTAL2_DIRECTORY, f"portal2/{file}"))
        
            # total demo duration
            #duration = 0.0

            with open(f"{PORTAL2_DIRECTORY}/portal2/cfg/autoexec.cfg", "w") as f:
                f.write("plugin_load sar\n")
                f.write("sar_fast_load_preset full\n")
                f.write("sar_disable_no_focus_sleep 1\n")

                f.write("sar_on_demo_stop quit\n")
                #f.write(f"playdemo demos/{filename}\n")

                f.write("""
sv_cheats 1
sar_render_blend 1
sar_render_autostart 1
sar_render_autostop 1
sar_render_fps 60
sar_render_blend 1
sar_render_quality 40

sar_on_demo_start snd_restart
sar_demo_remove_broken 1
sar_demo_blacklist_all 1
sar_fast_load_preset sla
cl_enable_remote_splitscreen 1
sar_on_demo_start hwait 30 +remote_view

sar_on_config_exec volume 0.3
sar_on_config_exec crosshair 0
sar_on_config_exec gameinstructor_enable 0
sar_quickhud_mode 2
sar_quickhud_set_texture crosshair/720quickhud
sar_crosshair_mode 1
cl_crosshairgap 6

sar_hud_y 10000
hud_saytext_time 0
sar_disable_coop_score_hud 1
sar_disable_challenge_stats_hud 1
sar_speedrun_start_on_load 0
sar_toast_disable 1
viewmodel_offset_x 0
cl_showpos 0
contimes 0
developer 0
net_graph 0

demo_interplimit 6000
demo_interpolateview 1
portal_draw_ghosting 1
dsp_enhance_stereo 1
mat_aaquality 2
mat_antialias 8
mat_envmapsize 512
mat_forceaniso 16
mat_postprocess_x 8
mat_postprocess_y 8
mat_reducefillrate 0
mat_dof_enabled 1
mat_dof_quality 8388610
mat_hdr_enabled 1
mat_hdr_level 2
mat_motion_blur_enabled 1
mat_tessellationlevel 16
mat_tessellation_cornertangents 1
mat_tessellation_update_buffers 1
mat_tessellation_accgeometrytangents 1
mat_object_motion_blur_enable 1
mat_software_aa_quality 9
mat_software_aa_edge_threshold 0
mat_software_aa_strength 8
mat_software_aa_strength_vgui 8
mat_software_aa_blur_one_pixel_lines 1
mat_specular 1
mat_shadowstate 2
mat_parallaxmapsamplesmin 64
mat_parallaxmapsamplesmax 128
mat_queue_mode -1
mat_fastspecular 0
mat_wateroverlaysize 512
mat_picmip -10
r_portal_stencil_depth 9
r_avglight 3
r_maxmodeldecal 4096
r_RainRadius 2250
r_RainSplashPercentage 100
r_rootlod 0
r_staticprop_lod 0
r_shadowmaxrendered 1024
r_shadowrendertotexture 1
r_shadows 1
r_shadowlod 0
r_dlightsenable 1
r_drawallrenderables 1
r_frustumcullworld 0
r_WaterDrawReflection 1
r_WaterDrawRefraction 1
r_waterforceexpensive 1
r_waterforcereflectentities 1
r_shadowfromanyworldlight 1
r_portal_fastpath_max_ghost_recursion 32
r_lod 0
r_threaded_blobulator 1
r_threaded_particles 1
r_occlusion 1
r_unloadlightmaps 0
r_3dsky 1
r_queued_post_processing 0
r_cheapwaterstart 8096
r_cheapwaterend 9000
r_unlimitedrefract 1
cl_detaildist 8096
cl_detailfade 0
cl_maxrenderable_dist 8096
cl_ragdoll_collide 1
cl_shadowtextureoverlaysize 4096
cl_forcepreload 1
r_portal_use_pvs_optimization 0
""")

            
                f.write(f"playdemo demos/{filename}\n")
                f.write("quit")
            # mlugg: the game can sometimes freeze, either just from bad luck or from dodgy
            # demos. this is the maximum time the game can be open before we give up and
            # kill it 
            # samueL: random number I chose
            timeout = 90000#duration * settings.RENDER_TIMEOUT_FACTOR + settings.RENDER_TIMEOUT_BASE
       
        # do the render
            proc = await asyncio.subprocess.create_subprocess_exec("/home/portal/.steam/steam/ubuntu12_32/steam-runtime/run.sh", f"{PORTAL2_DIRECTORY}/portal2.sh", "-game", "portal2", "-steam", "-novid", "-windowed","-vulkan", "-w", "960", "-h", "540", "0", cwd=PORTAL2_DIRECTORY)
            try:
                await asyncio.wait_for(proc.communicate(), timeout)
            except asyncio.TimeoutError:
                # timeout
                 proc.kill()
    
        # mlugg: this might help make sure file handles are properly closed? idk
        #await asyncio.sleep(1)
async def main():
    print("wee woo")
    await render_demos()
if __name__ == "__main__":
    #thread1 = threading.Thread(target=main())
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
    pass
