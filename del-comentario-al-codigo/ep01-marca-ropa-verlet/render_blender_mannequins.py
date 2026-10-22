import bpy, os, math, shutil
from collections import deque
from bl_ext.user_default.mpfb.services.humanservice import HumanService
from bl_ext.user_default.mpfb.services.assetservice import AssetService
from bl_ext.user_default.mpfb.services.objectservice import ObjectService

OUT_DIR = "/Users/kevingonzalezlopez/Work/Mixiuh/laboratorio-ia/del-comentario-al-codigo/ep01-marca-ropa-verlet/app/assets/mannequins"
os.makedirs(OUT_DIR, exist_ok=True)


def build_character_scene(gender_mode):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    is_female = (gender_mode == 'female')

    macro = {
        'gender': 0.0 if is_female else 1.0,
        'age': 0.32 if is_female else 0.36,
        'muscle': 0.58 if is_female else 0.75,
        'weight': 0.48 if is_female else 0.52,
        'height': 0.56 if is_female else 0.62,
        'proportions': 0.58 if is_female else 0.55,
        'cupsize': 0.60 if is_female else 0.50,
        'firmness': 0.72 if is_female else 0.50,
        'race': {'caucasian': 0.65, 'african': 0.18, 'asian': 0.17}
    }
    basemesh = HumanService.create_human(
        mask_helpers=True, detailed_helpers=True, extra_vertex_groups=True,
        feet_on_ground=True, scale=0.1, macro_detail_dict=macro
    )
    rig = HumanService.add_builtin_rig(basemesh, 'default', import_weights=True)

    eyes_path = AssetService.find_asset_absolute_path('high-poly/high-poly.mhclo', 'eyes')
    eyes_obj = HumanService.add_mhclo_asset(eyes_path, basemesh, asset_type='eyes', subdiv_levels=2, material_type='NONE')

    proxy_rel = 'female_muscle_13442/female_muscle_13442.proxy' if is_female else 'male_muscle_13290/male_muscle_13290.proxy'
    human_info = {'proxy': proxy_rel, 'name': 'StudioMannequin'}
    HumanService._check_add_proxy(human_info, basemesh, subdiv_levels=2)
    proxy_obj = ObjectService.find_object_of_type_amongst_nearest_relatives(basemesh, 'Proxymeshes')

    clothes_rel = 'female_casualsuit01/female_casualsuit01.mhclo' if is_female else 'male_casualsuit06/male_casualsuit06.mhclo'
    clothes_path = AssetService.find_asset_absolute_path(clothes_rel, 'clothes')
    clothes = HumanService.add_mhclo_asset(clothes_path, basemesh, asset_type='clothes', subdiv_levels=2, material_type='MAKESKIN')

    # Pose arms & hands into a relaxed editorial studio lookbook stance
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.mode_set(mode='POSE')
    for side, sgn in [('L', 1.0), ('R', -1.0)]:
        b_sh = rig.pose.bones.get(f'shoulder01.{side}')
        b_ua1 = rig.pose.bones.get(f'upperarm01.{side}')
        b_la1 = rig.pose.bones.get(f'lowerarm01.{side}')
        b_wr = rig.pose.bones.get(f'wrist.{side}')
        if b_sh:
            b_sh.rotation_mode = 'XYZ'
            b_sh.rotation_euler = (0.0, 0.0, math.radians(-5.5 * sgn))
        if b_ua1:
            b_ua1.rotation_mode = 'XYZ'
            arm_drop = -22.5 if is_female else -21.0
            b_ua1.rotation_euler = (math.radians(-6.0), math.radians(8.0 * sgn), math.radians(arm_drop * sgn))
        if b_la1:
            b_la1.rotation_mode = 'XYZ'
            b_la1.rotation_euler = (math.radians(-8.0), 0.0, math.radians(-4.0 * sgn))
        if b_wr:
            b_wr.rotation_mode = 'XYZ'
            b_wr.rotation_euler = (math.radians(2.0), math.radians(10.0 * sgn), math.radians(-8.0 * sgn))
        b_th1 = rig.pose.bones.get(f'finger1-1.{side}')
        b_th2 = rig.pose.bones.get(f'finger1-2.{side}')
        if b_th1:
            b_th1.rotation_mode = 'XYZ'
            b_th1.rotation_euler = (math.radians(22.0), math.radians(6.0 * sgn), math.radians(-28.0 * sgn))
        if b_th2:
            b_th2.rotation_mode = 'XYZ'
            b_th2.rotation_euler = (math.radians(10.0), 0.0, math.radians(-8.0 * sgn))
        for f_idx in range(2, 6):
            for j_idx in range(1, 4):
                fb = rig.pose.bones.get(f'finger{f_idx}-{j_idx}.{side}')
                if fb:
                    fb.rotation_mode = 'XYZ'
                    curl = 10.0 + (f_idx - 2) * 2.5
                    fb.rotation_euler = (math.radians(curl), 0.0, 0.0)
    bpy.ops.object.mode_set(mode='OBJECT')

    # Warm Sculpted Studio Mannequin Material
    mannequin_mat = bpy.data.materials.new('SculptedMannequinMat')
    bsdf = mannequin_mat.node_tree.nodes.get('Principled BSDF')
    skin_col = (0.52, 0.34, 0.25, 1.0) if not is_female else (0.56, 0.38, 0.28, 1.0)
    bsdf.inputs['Base Color'].default_value = skin_col
    bsdf.inputs['Roughness'].default_value = 0.24
    bsdf.inputs['Subsurface Weight'].default_value = 0.10
    bsdf.inputs['Subsurface Radius'].default_value = (0.8, 0.32, 0.18)
    bsdf.inputs['Subsurface Scale'].default_value = 0.006
    bsdf.inputs['Coat Weight'].default_value = 0.44
    bsdf.inputs['Coat Roughness'].default_value = 0.14
    bsdf.inputs['Specular IOR Level'].default_value = 0.60

    for obj in [basemesh, proxy_obj, eyes_obj]:
        if obj:
            obj.data.materials.clear()
            obj.data.materials.append(mannequin_mat)

    # ShirtMat (Slot 0) & JeansMat (Slot 1)
    shirt_mat = clothes.data.materials[0]
    shirt_mat.name = 'ShirtMat'
    shirt_mat.use_backface_culling = False
    jeans_mat = shirt_mat.copy()
    jeans_mat.name = 'JeansMat'
    clothes.data.materials.append(jeans_mat)

    s_nodes = shirt_mat.node_tree.nodes
    clean_diff = '/tmp/clean_clothes_tex/female_clean_diffuse.png' if is_female else '/tmp/clean_clothes_tex/male_clean_diffuse.png'
    s_nodes['diffuseTexture'].image = bpy.data.images.load(clean_diff)
    if is_female:
        s_nodes['normalmapTexture'].image = bpy.data.images.load('/tmp/clean_clothes_tex/female_clean_normal.png')
        s_nodes['normalmapTexture'].image.colorspace_settings.name = 'Non-Color'
    s_nodes['normalmap'].inputs['Strength'].default_value = 2.2 if not is_female else 1.85
    s_bsdf = s_nodes['Principled BSDF']
    s_bsdf.inputs['Roughness'].default_value = 0.85
    s_bsdf.inputs['Sheen Weight'].default_value = 0.55
    s_bsdf.inputs['Sheen Roughness'].default_value = 0.60

    # Dark Studio Indigo/Charcoal Selvedge Denim Jeans
    j_nodes = jeans_mat.node_tree.nodes
    j_nodes['diffuseIntensity'].blend_type = 'MULTIPLY'
    j_nodes['diffuseIntensity'].inputs[1].default_value = (0.28, 0.31, 0.38, 1.0)
    j_nodes['diffuseIntensity'].inputs[0].default_value = 0.82
    j_nodes['Principled BSDF'].inputs['Roughness'].default_value = 0.80

    # Assign Slot 0 to Shirt component, Slot 1 to Jeans component + create ShirtOnly vertex group
    mesh = clothes.data
    adj = {i: [] for i in range(len(mesh.vertices))}
    for poly in mesh.polygons:
        vs = list(poly.vertices)
        for i in range(len(vs)):
            for j in range(i+1, len(vs)):
                adj[vs[i]].append(vs[j])
                adj[vs[j]].append(vs[i])
    visited = set()
    comps = []
    for v in range(len(mesh.vertices)):
        if v not in visited:
            q = deque([v])
            visited.add(v)
            comp = set()
            while q:
                cur = q.popleft()
                comp.add(cur)
                for nxt in adj[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            comps.append(comp)
    comps.sort(key=lambda c: sum(mesh.vertices[v].co.z for v in c)/len(c), reverse=True)
    shirt_verts = list(comps[0])
    shirt_set = comps[0]
    for poly in mesh.polygons:
        poly.material_index = 0 if poly.vertices[0] in shirt_set else 1

    vg_shirt = clothes.vertex_groups.new(name='ShirtOnlyGroup')
    vg_shirt.add(shirt_verts, 1.0, 'REPLACE')

    # Add Mask modifier on clothes (before Subdivision) so we can cleanly hide Jeans at geometry level
    # Remove existing Subsurf and re-add after Mask so modifier order is Armature -> Mask -> Subsurf
    for mod in list(clothes.modifiers):
        if mod.type == 'SUBSURF':
            clothes.modifiers.remove(mod)
    mask_mod = clothes.modifiers.new('ShirtOnlyMask', 'MASK')
    mask_mod.vertex_group = 'ShirtOnlyGroup'
    mask_mod.show_viewport = False
    mask_mod.show_render = False
    sub_mod = clothes.modifiers.new('Subdivision', 'SUBSURF')
    sub_mod.levels = 2
    sub_mod.render_levels = 2

    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            for mod in obj.modifiers:
                if mod.type == 'SUBSURF':
                    mod.levels = 2
                    mod.render_levels = 2

    bpy.context.view_layer.update()
    depsgraph = bpy.context.evaluated_depsgraph_get()
    eval_proxy = proxy_obj.evaluated_get(depsgraph)
    zs = [(eval_proxy.matrix_world @ v.co).z for v in eval_proxy.data.vertices]
    z_top = max(zs)

    # Studio Camera & Lights
    cam_data = bpy.data.cameras.new('StudioCam')
    cam_data.lens = 75
    cam = bpy.data.objects.new('StudioCam', cam_data)
    bpy.context.scene.collection.objects.link(cam)
    bpy.context.scene.camera = cam

    def make_light(name, energy, size, color):
        ld = bpy.data.lights.new(name, type='AREA')
        ld.energy = energy
        ld.color = color
        ld.size = size
        lo = bpy.data.objects.new(name, ld)
        bpy.context.scene.collection.objects.link(lo)
        return lo

    l_key = make_light('KeyLight', 150.0, 1.35, (1.0, 0.98, 0.95))
    l_fill = make_light('FillLight', 58.0, 1.8, (0.90, 0.95, 1.0))
    l_rim = make_light('RimLight', 105.0, 1.5, (0.85, 0.92, 1.0))

    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'GPU'
    prefs = bpy.context.preferences.addons['cycles'].preferences
    prefs.compute_device_type = 'METAL'
    prefs.get_devices()
    for d in prefs.devices:
        d.use = True
    scene.render.film_transparent = True
    scene.render.resolution_x = 760
    scene.render.resolution_y = 920

    def render_view(prefix_name, is_back, is_ghost_flat=False):
        if is_ghost_flat:
            z_center = z_top * 0.685
            cam_dist = z_top * 0.95
        else:
            span_z = z_top * 0.585
            z_center = z_top - span_z * 0.47
            cam_dist = span_z * 2.15

        if not is_back:
            cam.location = (0.0, -cam_dist, z_center)
            cam.rotation_euler = (math.radians(90.0), 0.0, 0.0)
        else:
            cam.location = (0.0, cam_dist, z_center)
            cam.rotation_euler = (math.radians(90.0), 0.0, math.radians(180.0))

        ysgn = 1.0 if is_back else -1.0
        rot_z_off = 180.0 if is_back else 0.0
        l_key.location = (-1.35 * (-ysgn), 1.75 * ysgn, z_center + 0.62)
        l_key.rotation_euler = tuple(math.radians(a) for a in (58, 0, -35 + rot_z_off))
        l_fill.location = (1.55 * (-ysgn), 1.65 * ysgn, z_center + 0.10)
        l_fill.rotation_euler = tuple(math.radians(a) for a in (72, 0, 42 + rot_z_off))
        l_rim.location = (0.0, -1.45 * ysgn, z_center + 0.72)
        l_rim.rotation_euler = tuple(math.radians(a) for a in (-55, 0, 180 + rot_z_off))

        # 1. Full Studio Pass (Mannequin + Jeans + White 300 GSM Shirt, or Ghost Shirt only for flat)
        for obj in [basemesh, proxy_obj, eyes_obj]:
            if obj:
                obj.hide_render = is_ghost_flat
        mask_mod.show_render = is_ghost_flat
        bsdf.inputs['Base Color'].default_value = skin_col
        bsdf.inputs['Roughness'].default_value = 0.24
        bsdf.inputs['Subsurface Weight'].default_value = 0.10
        bsdf.inputs['Coat Weight'].default_value = 0.44
        bsdf.inputs['Specular IOR Level'].default_value = 0.60

        scene.cycles.samples = 36
        scene.cycles.use_denoising = True
        scene.render.filepath = os.path.join(OUT_DIR, f"{prefix_name}_studio.png")
        bpy.ops.render.render(write_still=True)

        # 2. Shirt-Only Chroma Occlusion Pass (Jeans masked out via ShirtOnlyMask; Mannequin set to pure matte green occluder)
        if not is_ghost_flat:
            mask_mod.show_render = True
            bsdf.inputs['Base Color'].default_value = (0.0, 1.0, 0.0, 1.0)
            bsdf.inputs['Roughness'].default_value = 1.0
            bsdf.inputs['Subsurface Weight'].default_value = 0.0
            bsdf.inputs['Coat Weight'].default_value = 0.0
            bsdf.inputs['Specular IOR Level'].default_value = 0.0
            scene.cycles.samples = 24
            scene.cycles.use_denoising = True
            scene.render.filepath = os.path.join(OUT_DIR, f"{prefix_name}_shirt_only.png")
            bpy.ops.render.render(write_still=True)
        else:
            shutil.copyfile(
                os.path.join(OUT_DIR, f"{prefix_name}_studio.png"),
                os.path.join(OUT_DIR, f"{prefix_name}_shirt_only.png")
            )

    if not is_female:
        render_view("male_front", is_back=False, is_ghost_flat=False)
        render_view("male_back", is_back=True, is_ghost_flat=False)
        render_view("flat_front", is_back=False, is_ghost_flat=True)
        render_view("flat_back", is_back=True, is_ghost_flat=True)
    else:
        render_view("female_front", is_back=False, is_ghost_flat=False)
        render_view("female_back", is_back=True, is_ghost_flat=False)


build_character_scene('male')
build_character_scene('female')
print("ALL 6 VIEWS RENDERED IN BLENDER!")
