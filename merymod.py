#mery mod

import pymel.core as pm
import maya.cmds as cmds

def keyAll():
    if getAttr("Mery_ac_cn_global.tx", k=1) or getAttr("Mery_ac_cn_global.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_global.tx")
    if getAttr("Mery_ac_lf_arm_control.tx", k=1) or getAttr("Mery_ac_lf_arm_control.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_arm_control.tx")
    if getAttr("Mery_ac_lf_elbowPivot.tx", k=1) or getAttr("Mery_ac_lf_elbowPivot.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_elbowPivot.tx")
    if getAttr("Mery_ac_lf_ikhand.tx", k=1) or getAttr("Mery_ac_lf_ikhand.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_ikhand.tx")
    if getAttr("Mery_ac_lf_clavicle.tx", k=1) or getAttr("Mery_ac_lf_clavicle.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_clavicle.tx")
    if getAttr("Mery_ac_cn_tongue4.tx", k=1) or getAttr("Mery_ac_cn_tongue4.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue4.tx")
    if getAttr("Mery_ac_cn_tongue3.tx", k=1) or getAttr("Mery_ac_cn_tongue3.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue3.tx")
    if getAttr("Mery_ac_cn_tongue2.tx", k=1) or getAttr("Mery_ac_cn_tongue2.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue2.tx")
    if getAttr("Mery_ac_up_teeth.tx", k=1) or getAttr("Mery_ac_up_teeth.tx", channelBox=1):
        setKeyframe("Mery_ac_up_teeth.tx")
    if getAttr("Mery_ac_cn_head.tx", k=1) or getAttr("Mery_ac_cn_head.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_head.tx")
    if getAttr("Mery_ac_cn_neck.tx", k=1) or getAttr("Mery_ac_cn_neck.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_neck.tx")
    if getAttr("Mery_ac_cn_tongue1.tx", k=1) or getAttr("Mery_ac_cn_tongue1.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue1.tx")
    if getAttr("Mery_ac_lf_eye.tx", k=1) or getAttr("Mery_ac_lf_eye.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_eye.tx")
    if getAttr("Mery_ac_rg_eye.tx", k=1) or getAttr("Mery_ac_rg_eye.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_eye.tx")
    if getAttr("Mery_ac_cn_eyes.tx", k=1) or getAttr("Mery_ac_cn_eyes.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_eyes.tx")
    if getAttr("Mery_ac_dw_teeth.tx", k=1) or getAttr("Mery_ac_dw_teeth.tx", channelBox=1):
        setKeyframe("Mery_ac_dw_teeth.tx")
    if getAttr("Mery_ac_cn_hip.tx", k=1) or getAttr("Mery_ac_cn_hip.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_hip.tx")
    if getAttr("Mery_ac_lf_breast.tx", k=1) or getAttr("Mery_ac_lf_breast.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_breast.tx")
    if getAttr("Mery_ac_rg_breast.tx", k=1) or getAttr("Mery_ac_rg_breast.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_breast.tx")
    if getAttr("Mery_ac_cn_chest.tx", k=1) or getAttr("Mery_ac_cn_chest.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_chest.tx")
    if getAttr("Mery_ac_cn_fkback02.tx", k=1) or getAttr("Mery_ac_cn_fkback02.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback02.tx")
    if getAttr("Mery_ac_cn_fkback01.tx", k=1) or getAttr("Mery_ac_cn_fkback01.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback01.tx")
    if getAttr("Mery_ac_cn_torso.tx", k=1) or getAttr("Mery_ac_cn_torso.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_torso.tx")
    if getAttr("Mery_ac_lf_index02.tx", k=1) or getAttr("Mery_ac_lf_index02.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_index02.tx")
    if getAttr("Mery_ac_lf_index01.tx", k=1) or getAttr("Mery_ac_lf_index01.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_index01.tx")
    if getAttr("Mery_ac_lf_index_base.tx", k=1) or getAttr("Mery_ac_lf_index_base.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_index_base.tx")
    if getAttr("Mery_ac_lf_middle03.tx", k=1) or getAttr("Mery_ac_lf_middle03.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle03.tx")
    if getAttr("Mery_ac_lf_middle02.tx", k=1) or getAttr("Mery_ac_lf_middle02.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle02.tx")
    if getAttr("Mery_ac_lf_middle01.tx", k=1) or getAttr("Mery_ac_lf_middle01.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle01.tx")
    if getAttr("Mery_ac_cn_vis.tx", k=1) or getAttr("Mery_ac_cn_vis.tx", channelBox=1):
        setKeyframe("Mery_ac_cn_vis.tx")
    if getAttr("Mery_ac_lf_hand_cup.tx", k=1) or getAttr("Mery_ac_lf_hand_cup.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_hand_cup.tx")
    if getAttr("Mery_ac_lf_thumb03.tx", k=1) or getAttr("Mery_ac_lf_thumb03.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb03.tx")
    if getAttr("Mery_ac_lf_thumb02.tx", k=1) or getAttr("Mery_ac_lf_thumb02.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb02.tx")
    if getAttr("Mery_ac_lf_thumb01.tx", k=1) or getAttr("Mery_ac_lf_thumb01.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb01.tx")
    if getAttr("Mery_ac_lf_index03.tx", k=1) or getAttr("Mery_ac_lf_index03.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_index03.tx")
    if getAttr("Mery_ac_lf_middle_base.tx", k=1) or getAttr("Mery_ac_lf_middle_base.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle_base.tx")
    if getAttr("Mery_ac_lf_ring03.tx", k=1) or getAttr("Mery_ac_lf_ring03.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring03.tx")
    if getAttr("Mery_ac_lf_ring02.tx", k=1) or getAttr("Mery_ac_lf_ring02.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring02.tx")
    if getAttr("Mery_ac_lf_ring01.tx", k=1) or getAttr("Mery_ac_lf_ring01.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring01.tx")
    if getAttr("Mery_ac_lf_ring_base.tx", k=1) or getAttr("Mery_ac_lf_ring_base.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring_base.tx")
    if getAttr("Mery_ac_rg_hand_cup.tx", k=1) or getAttr("Mery_ac_rg_hand_cup.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_hand_cup.tx")
    if getAttr("Mery_ac_rg_thumb03.tx", k=1) or getAttr("Mery_ac_rg_thumb03.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb03.tx")
    if getAttr("Mery_ac_lf_pinky03.tx", k=1) or getAttr("Mery_ac_lf_pinky03.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky03.tx")
    if getAttr("Mery_ac_lf_pinky02.tx", k=1) or getAttr("Mery_ac_lf_pinky02.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky02.tx")
    if getAttr("Mery_ac_lf_pinky01.tx", k=1) or getAttr("Mery_ac_lf_pinky01.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky01.tx")
    if getAttr("Mery_ac_lf_pinky_base.tx", k=1) or getAttr("Mery_ac_lf_pinky_base.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky_base.tx")
    if getAttr("Mery_ac_rg_middle03.tx", k=1) or getAttr("Mery_ac_rg_middle03.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle03.tx")
    if getAttr("Mery_ac_rg_middle02.tx", k=1) or getAttr("Mery_ac_rg_middle02.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle02.tx")
    if getAttr("Mery_ac_rg_middle01.tx", k=1) or getAttr("Mery_ac_rg_middle01.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle01.tx")
    if getAttr("Mery_ac_rg_middle_base.tx", k=1) or getAttr("Mery_ac_rg_middle_base.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle_base.tx")
    if getAttr("Mery_ac_rg_ring03.tx", k=1) or getAttr("Mery_ac_rg_ring03.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring03.tx")
    if getAttr("Mery_ac_rg_ring02.tx", k=1) or getAttr("Mery_ac_rg_ring02.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring02.tx")
    if getAttr("Mery_ac_rg_thumb02.tx", k=1) or getAttr("Mery_ac_rg_thumb02.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb02.tx")
    if getAttr("Mery_ac_rg_thumb01.tx", k=1) or getAttr("Mery_ac_rg_thumb01.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb01.tx")
    if getAttr("Mery_ac_rg_index03.tx", k=1) or getAttr("Mery_ac_rg_index03.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_index03.tx")
    if getAttr("Mery_ac_rg_index02.tx", k=1) or getAttr("Mery_ac_rg_index02.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_index02.tx")
    if getAttr("Mery_ac_rg_index01.tx", k=1) or getAttr("Mery_ac_rg_index01.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_index01.tx")
    if getAttr("Mery_ac_rg_index_base.tx", k=1) or getAttr("Mery_ac_rg_index_base.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_index_base.tx")
    if getAttr("Mery_ac_rg_ring01.tx", k=1) or getAttr("Mery_ac_rg_ring01.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring01.tx")
    if getAttr("Mery_ac_rg_ring_base.tx", k=1) or getAttr("Mery_ac_rg_ring_base.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring_base.tx")
    if getAttr("Mery_ac_rg_pinky03.tx", k=1) or getAttr("Mery_ac_rg_pinky03.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky03.tx")
    if getAttr("Mery_ac_rg_pinky02.tx", k=1) or getAttr("Mery_ac_rg_pinky02.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky02.tx")
    if getAttr("Mery_ac_rg_pinky01.tx", k=1) or getAttr("Mery_ac_rg_pinky01.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky01.tx")
    if getAttr("Mery_ac_rg_pinky_base.tx", k=1) or getAttr("Mery_ac_rg_pinky_base.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky_base.tx")
    if getAttr("Mery_ac_rg_leg_control.tx", k=1) or getAttr("Mery_ac_rg_leg_control.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_leg_control.tx")
    if getAttr("Mery_ac_rg_kneePivot.tx", k=1) or getAttr("Mery_ac_rg_kneePivot.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_kneePivot.tx")
    if getAttr("Mery_ac_rg_ikfoot.tx", k=1) or getAttr("Mery_ac_rg_ikfoot.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.tx")
    if getAttr("Mery_ac_rg_toe.tx", k=1) or getAttr("Mery_ac_rg_toe.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_toe.tx")
    if getAttr("Mery_ac_lf_kneePivot.tx", k=1) or getAttr("Mery_ac_lf_kneePivot.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_kneePivot.tx")
    if getAttr("Mery_ac_lf_ikfoot.tx", k=1) or getAttr("Mery_ac_lf_ikfoot.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.tx")
    if getAttr("Mery_ac_lf_toe.tx", k=1) or getAttr("Mery_ac_lf_toe.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_toe.tx")
    if getAttr("Mery_ac_lf_leg_control.tx", k=1) or getAttr("Mery_ac_lf_leg_control.tx", channelBox=1):
        setKeyframe("Mery_ac_lf_leg_control.tx")
    if getAttr("Mery_ac_rg_arm_control.tx", k=1) or getAttr("Mery_ac_rg_arm_control.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_arm_control.tx")
    if getAttr("Mery_ac_rg_elbowPivot.tx", k=1) or getAttr("Mery_ac_rg_elbowPivot.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_elbowPivot.tx")
    if getAttr("Mery_ac_rg_ikhand.tx", k=1) or getAttr("Mery_ac_rg_ikhand.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_ikhand.tx")
    if getAttr("Mery_ac_rg_clavicle.tx", k=1) or getAttr("Mery_ac_rg_clavicle.tx", channelBox=1):
        setKeyframe("Mery_ac_rg_clavicle.tx")
    if getAttr("Mery_ac_cn_global.ty", k=1) or getAttr("Mery_ac_cn_global.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_global.ty")
    if getAttr("Mery_ac_lf_arm_control.ty", k=1) or getAttr("Mery_ac_lf_arm_control.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_arm_control.ty")
    if getAttr("Mery_ac_lf_elbowPivot.ty", k=1) or getAttr("Mery_ac_lf_elbowPivot.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_elbowPivot.ty")
    if getAttr("Mery_ac_lf_ikhand.ty", k=1) or getAttr("Mery_ac_lf_ikhand.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_ikhand.ty")
    if getAttr("Mery_ac_lf_clavicle.ty", k=1) or getAttr("Mery_ac_lf_clavicle.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_clavicle.ty")
    if getAttr("Mery_ac_cn_tongue4.ty", k=1) or getAttr("Mery_ac_cn_tongue4.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue4.ty")
    if getAttr("Mery_ac_cn_tongue3.ty", k=1) or getAttr("Mery_ac_cn_tongue3.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue3.ty")
    if getAttr("Mery_ac_cn_tongue2.ty", k=1) or getAttr("Mery_ac_cn_tongue2.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue2.ty")
    if getAttr("Mery_ac_up_teeth.ty", k=1) or getAttr("Mery_ac_up_teeth.ty", channelBox=1):
        setKeyframe("Mery_ac_up_teeth.ty")
    if getAttr("Mery_ac_cn_head.ty", k=1) or getAttr("Mery_ac_cn_head.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_head.ty")
    if getAttr("Mery_ac_cn_neck.ty", k=1) or getAttr("Mery_ac_cn_neck.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_neck.ty")
    if getAttr("Mery_ac_cn_tongue1.ty", k=1) or getAttr("Mery_ac_cn_tongue1.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue1.ty")
    if getAttr("Mery_ac_lf_eye.ty", k=1) or getAttr("Mery_ac_lf_eye.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_eye.ty")
    if getAttr("Mery_ac_rg_eye.ty", k=1) or getAttr("Mery_ac_rg_eye.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_eye.ty")
    if getAttr("Mery_ac_cn_eyes.ty", k=1) or getAttr("Mery_ac_cn_eyes.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_eyes.ty")
    if getAttr("Mery_ac_dw_teeth.ty", k=1) or getAttr("Mery_ac_dw_teeth.ty", channelBox=1):
        setKeyframe("Mery_ac_dw_teeth.ty")
    if getAttr("Mery_ac_cn_hip.ty", k=1) or getAttr("Mery_ac_cn_hip.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_hip.ty")
    if getAttr("Mery_ac_lf_breast.ty", k=1) or getAttr("Mery_ac_lf_breast.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_breast.ty")
    if getAttr("Mery_ac_rg_breast.ty", k=1) or getAttr("Mery_ac_rg_breast.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_breast.ty")
    if getAttr("Mery_ac_cn_chest.ty", k=1) or getAttr("Mery_ac_cn_chest.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_chest.ty")
    if getAttr("Mery_ac_cn_fkback02.ty", k=1) or getAttr("Mery_ac_cn_fkback02.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback02.ty")
    if getAttr("Mery_ac_cn_fkback01.ty", k=1) or getAttr("Mery_ac_cn_fkback01.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback01.ty")
    if getAttr("Mery_ac_cn_torso.ty", k=1) or getAttr("Mery_ac_cn_torso.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_torso.ty")
    if getAttr("Mery_ac_lf_index02.ty", k=1) or getAttr("Mery_ac_lf_index02.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_index02.ty")
    if getAttr("Mery_ac_lf_index01.ty", k=1) or getAttr("Mery_ac_lf_index01.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_index01.ty")
    if getAttr("Mery_ac_lf_index_base.ty", k=1) or getAttr("Mery_ac_lf_index_base.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_index_base.ty")
    if getAttr("Mery_ac_lf_middle03.ty", k=1) or getAttr("Mery_ac_lf_middle03.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_middle03.ty")
    if getAttr("Mery_ac_lf_middle02.ty", k=1) or getAttr("Mery_ac_lf_middle02.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_middle02.ty")
    if getAttr("Mery_ac_lf_middle01.ty", k=1) or getAttr("Mery_ac_lf_middle01.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_middle01.ty")
    if getAttr("Mery_ac_cn_vis.ty", k=1) or getAttr("Mery_ac_cn_vis.ty", channelBox=1):
        setKeyframe("Mery_ac_cn_vis.ty")
    if getAttr("Mery_ac_lf_hand_cup.ty", k=1) or getAttr("Mery_ac_lf_hand_cup.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_hand_cup.ty")
    if getAttr("Mery_ac_lf_thumb03.ty", k=1) or getAttr("Mery_ac_lf_thumb03.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb03.ty")
    if getAttr("Mery_ac_lf_thumb02.ty", k=1) or getAttr("Mery_ac_lf_thumb02.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb02.ty")
    if getAttr("Mery_ac_lf_thumb01.ty", k=1) or getAttr("Mery_ac_lf_thumb01.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb01.ty")
    if getAttr("Mery_ac_lf_index03.ty", k=1) or getAttr("Mery_ac_lf_index03.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_index03.ty")
    if getAttr("Mery_ac_lf_middle_base.ty", k=1) or getAttr("Mery_ac_lf_middle_base.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_middle_base.ty")
    if getAttr("Mery_ac_lf_ring03.ty", k=1) or getAttr("Mery_ac_lf_ring03.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_ring03.ty")
    if getAttr("Mery_ac_lf_ring02.ty", k=1) or getAttr("Mery_ac_lf_ring02.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_ring02.ty")
    if getAttr("Mery_ac_lf_ring01.ty", k=1) or getAttr("Mery_ac_lf_ring01.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_ring01.ty")
    if getAttr("Mery_ac_lf_ring_base.ty", k=1) or getAttr("Mery_ac_lf_ring_base.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_ring_base.ty")
    if getAttr("Mery_ac_rg_hand_cup.ty", k=1) or getAttr("Mery_ac_rg_hand_cup.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_hand_cup.ty")
    if getAttr("Mery_ac_rg_thumb03.ty", k=1) or getAttr("Mery_ac_rg_thumb03.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb03.ty")
    if getAttr("Mery_ac_lf_pinky03.ty", k=1) or getAttr("Mery_ac_lf_pinky03.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky03.ty")
    if getAttr("Mery_ac_lf_pinky02.ty", k=1) or getAttr("Mery_ac_lf_pinky02.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky02.ty")
    if getAttr("Mery_ac_lf_pinky01.ty", k=1) or getAttr("Mery_ac_lf_pinky01.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky01.ty")
    if getAttr("Mery_ac_lf_pinky_base.ty", k=1) or getAttr("Mery_ac_lf_pinky_base.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky_base.ty")
    if getAttr("Mery_ac_rg_middle03.ty", k=1) or getAttr("Mery_ac_rg_middle03.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_middle03.ty")
    if getAttr("Mery_ac_rg_middle02.ty", k=1) or getAttr("Mery_ac_rg_middle02.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_middle02.ty")
    if getAttr("Mery_ac_rg_middle01.ty", k=1) or getAttr("Mery_ac_rg_middle01.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_middle01.ty")
    if getAttr("Mery_ac_rg_middle_base.ty", k=1) or getAttr("Mery_ac_rg_middle_base.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_middle_base.ty")
    if getAttr("Mery_ac_rg_ring03.ty", k=1) or getAttr("Mery_ac_rg_ring03.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_ring03.ty")
    if getAttr("Mery_ac_rg_ring02.ty", k=1) or getAttr("Mery_ac_rg_ring02.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_ring02.ty")
    if getAttr("Mery_ac_rg_thumb02.ty", k=1) or getAttr("Mery_ac_rg_thumb02.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb02.ty")
    if getAttr("Mery_ac_rg_thumb01.ty", k=1) or getAttr("Mery_ac_rg_thumb01.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb01.ty")
    if getAttr("Mery_ac_rg_index03.ty", k=1) or getAttr("Mery_ac_rg_index03.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_index03.ty")
    if getAttr("Mery_ac_rg_index02.ty", k=1) or getAttr("Mery_ac_rg_index02.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_index02.ty")
    if getAttr("Mery_ac_rg_index01.ty", k=1) or getAttr("Mery_ac_rg_index01.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_index01.ty")
    if getAttr("Mery_ac_rg_index_base.ty", k=1) or getAttr("Mery_ac_rg_index_base.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_index_base.ty")
    if getAttr("Mery_ac_rg_ring01.ty", k=1) or getAttr("Mery_ac_rg_ring01.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_ring01.ty")
    if getAttr("Mery_ac_rg_ring_base.ty", k=1) or getAttr("Mery_ac_rg_ring_base.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_ring_base.ty")
    if getAttr("Mery_ac_rg_pinky03.ty", k=1) or getAttr("Mery_ac_rg_pinky03.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky03.ty")
    if getAttr("Mery_ac_rg_pinky02.ty", k=1) or getAttr("Mery_ac_rg_pinky02.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky02.ty")
    if getAttr("Mery_ac_rg_pinky01.ty", k=1) or getAttr("Mery_ac_rg_pinky01.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky01.ty")
    if getAttr("Mery_ac_rg_pinky_base.ty", k=1) or getAttr("Mery_ac_rg_pinky_base.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky_base.ty")
    if getAttr("Mery_ac_rg_leg_control.ty", k=1) or getAttr("Mery_ac_rg_leg_control.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_leg_control.ty")
    if getAttr("Mery_ac_rg_kneePivot.ty", k=1) or getAttr("Mery_ac_rg_kneePivot.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_kneePivot.ty")
    if getAttr("Mery_ac_rg_ikfoot.ty", k=1) or getAttr("Mery_ac_rg_ikfoot.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.ty")
    if getAttr("Mery_ac_rg_toe.ty", k=1) or getAttr("Mery_ac_rg_toe.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_toe.ty")
    if getAttr("Mery_ac_lf_kneePivot.ty", k=1) or getAttr("Mery_ac_lf_kneePivot.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_kneePivot.ty")
    if getAttr("Mery_ac_lf_ikfoot.ty", k=1) or getAttr("Mery_ac_lf_ikfoot.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.ty")
    if getAttr("Mery_ac_lf_toe.ty", k=1) or getAttr("Mery_ac_lf_toe.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_toe.ty")
    if getAttr("Mery_ac_lf_leg_control.ty", k=1) or getAttr("Mery_ac_lf_leg_control.ty", channelBox=1):
        setKeyframe("Mery_ac_lf_leg_control.ty")
    if getAttr("Mery_ac_rg_arm_control.ty", k=1) or getAttr("Mery_ac_rg_arm_control.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_arm_control.ty")
    if getAttr("Mery_ac_rg_elbowPivot.ty", k=1) or getAttr("Mery_ac_rg_elbowPivot.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_elbowPivot.ty")
    if getAttr("Mery_ac_rg_ikhand.ty", k=1) or getAttr("Mery_ac_rg_ikhand.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_ikhand.ty")
    if getAttr("Mery_ac_rg_clavicle.ty", k=1) or getAttr("Mery_ac_rg_clavicle.ty", channelBox=1):
        setKeyframe("Mery_ac_rg_clavicle.ty")
    if getAttr("Mery_ac_cn_global.tz", k=1) or getAttr("Mery_ac_cn_global.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_global.tz")
    if getAttr("Mery_ac_lf_arm_control.tz", k=1) or getAttr("Mery_ac_lf_arm_control.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_arm_control.tz")
    if getAttr("Mery_ac_lf_elbowPivot.tz", k=1) or getAttr("Mery_ac_lf_elbowPivot.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_elbowPivot.tz")
    if getAttr("Mery_ac_lf_ikhand.tz", k=1) or getAttr("Mery_ac_lf_ikhand.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_ikhand.tz")
    if getAttr("Mery_ac_lf_clavicle.tz", k=1) or getAttr("Mery_ac_lf_clavicle.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_clavicle.tz")
    if getAttr("Mery_ac_cn_tongue4.tz", k=1) or getAttr("Mery_ac_cn_tongue4.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue4.tz")
    if getAttr("Mery_ac_cn_tongue3.tz", k=1) or getAttr("Mery_ac_cn_tongue3.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue3.tz")
    if getAttr("Mery_ac_cn_tongue2.tz", k=1) or getAttr("Mery_ac_cn_tongue2.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue2.tz")
    if getAttr("Mery_ac_up_teeth.tz", k=1) or getAttr("Mery_ac_up_teeth.tz", channelBox=1):
        setKeyframe("Mery_ac_up_teeth.tz")
    if getAttr("Mery_ac_cn_head.tz", k=1) or getAttr("Mery_ac_cn_head.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_head.tz")
    if getAttr("Mery_ac_cn_neck.tz", k=1) or getAttr("Mery_ac_cn_neck.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_neck.tz")
    if getAttr("Mery_ac_cn_tongue1.tz", k=1) or getAttr("Mery_ac_cn_tongue1.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue1.tz")
    if getAttr("Mery_ac_lf_eye.tz", k=1) or getAttr("Mery_ac_lf_eye.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_eye.tz")
    if getAttr("Mery_ac_rg_eye.tz", k=1) or getAttr("Mery_ac_rg_eye.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_eye.tz")
    if getAttr("Mery_ac_cn_eyes.tz", k=1) or getAttr("Mery_ac_cn_eyes.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_eyes.tz")
    if getAttr("Mery_ac_dw_teeth.tz", k=1) or getAttr("Mery_ac_dw_teeth.tz", channelBox=1):
        setKeyframe("Mery_ac_dw_teeth.tz")
    if getAttr("Mery_ac_cn_hip.tz", k=1) or getAttr("Mery_ac_cn_hip.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_hip.tz")
    if getAttr("Mery_ac_lf_breast.tz", k=1) or getAttr("Mery_ac_lf_breast.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_breast.tz")
    if getAttr("Mery_ac_rg_breast.tz", k=1) or getAttr("Mery_ac_rg_breast.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_breast.tz")
    if getAttr("Mery_ac_cn_chest.tz", k=1) or getAttr("Mery_ac_cn_chest.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_chest.tz")
    if getAttr("Mery_ac_cn_fkback02.tz", k=1) or getAttr("Mery_ac_cn_fkback02.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback02.tz")
    if getAttr("Mery_ac_cn_fkback01.tz", k=1) or getAttr("Mery_ac_cn_fkback01.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback01.tz")
    if getAttr("Mery_ac_cn_torso.tz", k=1) or getAttr("Mery_ac_cn_torso.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_torso.tz")
    if getAttr("Mery_ac_lf_index02.tz", k=1) or getAttr("Mery_ac_lf_index02.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_index02.tz")
    if getAttr("Mery_ac_lf_index01.tz", k=1) or getAttr("Mery_ac_lf_index01.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_index01.tz")
    if getAttr("Mery_ac_lf_index_base.tz", k=1) or getAttr("Mery_ac_lf_index_base.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_index_base.tz")
    if getAttr("Mery_ac_lf_middle03.tz", k=1) or getAttr("Mery_ac_lf_middle03.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle03.tz")
    if getAttr("Mery_ac_lf_middle02.tz", k=1) or getAttr("Mery_ac_lf_middle02.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle02.tz")
    if getAttr("Mery_ac_lf_middle01.tz", k=1) or getAttr("Mery_ac_lf_middle01.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle01.tz")
    if getAttr("Mery_ac_cn_vis.tz", k=1) or getAttr("Mery_ac_cn_vis.tz", channelBox=1):
        setKeyframe("Mery_ac_cn_vis.tz")
    if getAttr("Mery_ac_lf_hand_cup.tz", k=1) or getAttr("Mery_ac_lf_hand_cup.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_hand_cup.tz")
    if getAttr("Mery_ac_lf_thumb03.tz", k=1) or getAttr("Mery_ac_lf_thumb03.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb03.tz")
    if getAttr("Mery_ac_lf_thumb02.tz", k=1) or getAttr("Mery_ac_lf_thumb02.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb02.tz")
    if getAttr("Mery_ac_lf_thumb01.tz", k=1) or getAttr("Mery_ac_lf_thumb01.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb01.tz")
    if getAttr("Mery_ac_lf_index03.tz", k=1) or getAttr("Mery_ac_lf_index03.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_index03.tz")
    if getAttr("Mery_ac_lf_middle_base.tz", k=1) or getAttr("Mery_ac_lf_middle_base.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle_base.tz")
    if getAttr("Mery_ac_lf_ring03.tz", k=1) or getAttr("Mery_ac_lf_ring03.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring03.tz")
    if getAttr("Mery_ac_lf_ring02.tz", k=1) or getAttr("Mery_ac_lf_ring02.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring02.tz")
    if getAttr("Mery_ac_lf_ring01.tz", k=1) or getAttr("Mery_ac_lf_ring01.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring01.tz")
    if getAttr("Mery_ac_lf_ring_base.tz", k=1) or getAttr("Mery_ac_lf_ring_base.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring_base.tz")
    if getAttr("Mery_ac_rg_hand_cup.tz", k=1) or getAttr("Mery_ac_rg_hand_cup.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_hand_cup.tz")
    if getAttr("Mery_ac_rg_thumb03.tz", k=1) or getAttr("Mery_ac_rg_thumb03.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb03.tz")
    if getAttr("Mery_ac_lf_pinky03.tz", k=1) or getAttr("Mery_ac_lf_pinky03.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky03.tz")
    if getAttr("Mery_ac_lf_pinky02.tz", k=1) or getAttr("Mery_ac_lf_pinky02.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky02.tz")
    if getAttr("Mery_ac_lf_pinky01.tz", k=1) or getAttr("Mery_ac_lf_pinky01.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky01.tz")
    if getAttr("Mery_ac_lf_pinky_base.tz", k=1) or getAttr("Mery_ac_lf_pinky_base.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky_base.tz")
    if getAttr("Mery_ac_rg_middle03.tz", k=1) or getAttr("Mery_ac_rg_middle03.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle03.tz")
    if getAttr("Mery_ac_rg_middle02.tz", k=1) or getAttr("Mery_ac_rg_middle02.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle02.tz")
    if getAttr("Mery_ac_rg_middle01.tz", k=1) or getAttr("Mery_ac_rg_middle01.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle01.tz")
    if getAttr("Mery_ac_rg_middle_base.tz", k=1) or getAttr("Mery_ac_rg_middle_base.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle_base.tz")
    if getAttr("Mery_ac_rg_ring03.tz", k=1) or getAttr("Mery_ac_rg_ring03.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring03.tz")
    if getAttr("Mery_ac_rg_ring02.tz", k=1) or getAttr("Mery_ac_rg_ring02.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring02.tz")
    if getAttr("Mery_ac_rg_thumb02.tz", k=1) or getAttr("Mery_ac_rg_thumb02.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb02.tz")
    if getAttr("Mery_ac_rg_thumb01.tz", k=1) or getAttr("Mery_ac_rg_thumb01.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb01.tz")
    if getAttr("Mery_ac_rg_index03.tz", k=1) or getAttr("Mery_ac_rg_index03.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_index03.tz")
    if getAttr("Mery_ac_rg_index02.tz", k=1) or getAttr("Mery_ac_rg_index02.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_index02.tz")
    if getAttr("Mery_ac_rg_index01.tz", k=1) or getAttr("Mery_ac_rg_index01.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_index01.tz")
    if getAttr("Mery_ac_rg_index_base.tz", k=1) or getAttr("Mery_ac_rg_index_base.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_index_base.tz")
    if getAttr("Mery_ac_rg_ring01.tz", k=1) or getAttr("Mery_ac_rg_ring01.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring01.tz")
    if getAttr("Mery_ac_rg_ring_base.tz", k=1) or getAttr("Mery_ac_rg_ring_base.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring_base.tz")
    if getAttr("Mery_ac_rg_pinky03.tz", k=1) or getAttr("Mery_ac_rg_pinky03.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky03.tz")
    if getAttr("Mery_ac_rg_pinky02.tz", k=1) or getAttr("Mery_ac_rg_pinky02.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky02.tz")
    if getAttr("Mery_ac_rg_pinky01.tz", k=1) or getAttr("Mery_ac_rg_pinky01.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky01.tz")
    if getAttr("Mery_ac_rg_pinky_base.tz", k=1) or getAttr("Mery_ac_rg_pinky_base.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky_base.tz")
    if getAttr("Mery_ac_rg_leg_control.tz", k=1) or getAttr("Mery_ac_rg_leg_control.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_leg_control.tz")
    if getAttr("Mery_ac_rg_kneePivot.tz", k=1) or getAttr("Mery_ac_rg_kneePivot.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_kneePivot.tz")
    if getAttr("Mery_ac_rg_ikfoot.tz", k=1) or getAttr("Mery_ac_rg_ikfoot.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.tz")
    if getAttr("Mery_ac_rg_toe.tz", k=1) or getAttr("Mery_ac_rg_toe.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_toe.tz")
    if getAttr("Mery_ac_lf_kneePivot.tz", k=1) or getAttr("Mery_ac_lf_kneePivot.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_kneePivot.tz")
    if getAttr("Mery_ac_lf_ikfoot.tz", k=1) or getAttr("Mery_ac_lf_ikfoot.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.tz")
    if getAttr("Mery_ac_lf_toe.tz", k=1) or getAttr("Mery_ac_lf_toe.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_toe.tz")
    if getAttr("Mery_ac_lf_leg_control.tz", k=1) or getAttr("Mery_ac_lf_leg_control.tz", channelBox=1):
        setKeyframe("Mery_ac_lf_leg_control.tz")
    if getAttr("Mery_ac_rg_arm_control.tz", k=1) or getAttr("Mery_ac_rg_arm_control.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_arm_control.tz")
    if getAttr("Mery_ac_rg_elbowPivot.tz", k=1) or getAttr("Mery_ac_rg_elbowPivot.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_elbowPivot.tz")
    if getAttr("Mery_ac_rg_ikhand.tz", k=1) or getAttr("Mery_ac_rg_ikhand.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_ikhand.tz")
    if getAttr("Mery_ac_rg_clavicle.tz", k=1) or getAttr("Mery_ac_rg_clavicle.tz", channelBox=1):
        setKeyframe("Mery_ac_rg_clavicle.tz")
    if getAttr("Mery_ac_cn_global.rx", k=1) or getAttr("Mery_ac_cn_global.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_global.rx")
    if getAttr("Mery_ac_lf_arm_control.rx", k=1) or getAttr("Mery_ac_lf_arm_control.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_arm_control.rx")
    if getAttr("Mery_ac_lf_elbowPivot.rx", k=1) or getAttr("Mery_ac_lf_elbowPivot.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_elbowPivot.rx")
    if getAttr("Mery_ac_lf_ikhand.rx", k=1) or getAttr("Mery_ac_lf_ikhand.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_ikhand.rx")
    if getAttr("Mery_ac_lf_clavicle.rx", k=1) or getAttr("Mery_ac_lf_clavicle.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_clavicle.rx")
    if getAttr("Mery_ac_cn_tongue4.rx", k=1) or getAttr("Mery_ac_cn_tongue4.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue4.rx")
    if getAttr("Mery_ac_cn_tongue3.rx", k=1) or getAttr("Mery_ac_cn_tongue3.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue3.rx")
    if getAttr("Mery_ac_cn_tongue2.rx", k=1) or getAttr("Mery_ac_cn_tongue2.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue2.rx")
    if getAttr("Mery_ac_up_teeth.rx", k=1) or getAttr("Mery_ac_up_teeth.rx", channelBox=1):
        setKeyframe("Mery_ac_up_teeth.rx")
    if getAttr("Mery_ac_cn_head.rx", k=1) or getAttr("Mery_ac_cn_head.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_head.rx")
    if getAttr("Mery_ac_cn_neck.rx", k=1) or getAttr("Mery_ac_cn_neck.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_neck.rx")
    if getAttr("Mery_ac_cn_tongue1.rx", k=1) or getAttr("Mery_ac_cn_tongue1.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue1.rx")
    if getAttr("Mery_ac_lf_eye.rx", k=1) or getAttr("Mery_ac_lf_eye.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_eye.rx")
    if getAttr("Mery_ac_rg_eye.rx", k=1) or getAttr("Mery_ac_rg_eye.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_eye.rx")
    if getAttr("Mery_ac_cn_eyes.rx", k=1) or getAttr("Mery_ac_cn_eyes.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_eyes.rx")
    if getAttr("Mery_ac_dw_teeth.rx", k=1) or getAttr("Mery_ac_dw_teeth.rx", channelBox=1):
        setKeyframe("Mery_ac_dw_teeth.rx")
    if getAttr("Mery_ac_cn_hip.rx", k=1) or getAttr("Mery_ac_cn_hip.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_hip.rx")
    if getAttr("Mery_ac_lf_breast.rx", k=1) or getAttr("Mery_ac_lf_breast.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_breast.rx")
    if getAttr("Mery_ac_rg_breast.rx", k=1) or getAttr("Mery_ac_rg_breast.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_breast.rx")
    if getAttr("Mery_ac_cn_chest.rx", k=1) or getAttr("Mery_ac_cn_chest.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_chest.rx")
    if getAttr("Mery_ac_cn_fkback02.rx", k=1) or getAttr("Mery_ac_cn_fkback02.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback02.rx")
    if getAttr("Mery_ac_cn_fkback01.rx", k=1) or getAttr("Mery_ac_cn_fkback01.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback01.rx")
    if getAttr("Mery_ac_cn_torso.rx", k=1) or getAttr("Mery_ac_cn_torso.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_torso.rx")
    if getAttr("Mery_ac_lf_index02.rx", k=1) or getAttr("Mery_ac_lf_index02.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_index02.rx")
    if getAttr("Mery_ac_lf_index01.rx", k=1) or getAttr("Mery_ac_lf_index01.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_index01.rx")
    if getAttr("Mery_ac_lf_index_base.rx", k=1) or getAttr("Mery_ac_lf_index_base.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_index_base.rx")
    if getAttr("Mery_ac_lf_middle03.rx", k=1) or getAttr("Mery_ac_lf_middle03.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle03.rx")
    if getAttr("Mery_ac_lf_middle02.rx", k=1) or getAttr("Mery_ac_lf_middle02.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle02.rx")
    if getAttr("Mery_ac_lf_middle01.rx", k=1) or getAttr("Mery_ac_lf_middle01.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle01.rx")
    if getAttr("Mery_ac_cn_vis.rx", k=1) or getAttr("Mery_ac_cn_vis.rx", channelBox=1):
        setKeyframe("Mery_ac_cn_vis.rx")
    if getAttr("Mery_ac_lf_hand_cup.rx", k=1) or getAttr("Mery_ac_lf_hand_cup.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_hand_cup.rx")
    if getAttr("Mery_ac_lf_thumb03.rx", k=1) or getAttr("Mery_ac_lf_thumb03.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb03.rx")
    if getAttr("Mery_ac_lf_thumb02.rx", k=1) or getAttr("Mery_ac_lf_thumb02.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb02.rx")
    if getAttr("Mery_ac_lf_thumb01.rx", k=1) or getAttr("Mery_ac_lf_thumb01.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb01.rx")
    if getAttr("Mery_ac_lf_index03.rx", k=1) or getAttr("Mery_ac_lf_index03.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_index03.rx")
    if getAttr("Mery_ac_lf_middle_base.rx", k=1) or getAttr("Mery_ac_lf_middle_base.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_middle_base.rx")
    if getAttr("Mery_ac_lf_ring03.rx", k=1) or getAttr("Mery_ac_lf_ring03.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring03.rx")
    if getAttr("Mery_ac_lf_ring02.rx", k=1) or getAttr("Mery_ac_lf_ring02.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring02.rx")
    if getAttr("Mery_ac_lf_ring01.rx", k=1) or getAttr("Mery_ac_lf_ring01.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring01.rx")
    if getAttr("Mery_ac_lf_ring_base.rx", k=1) or getAttr("Mery_ac_lf_ring_base.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_ring_base.rx")
    if getAttr("Mery_ac_rg_hand_cup.rx", k=1) or getAttr("Mery_ac_rg_hand_cup.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_hand_cup.rx")
    if getAttr("Mery_ac_rg_thumb03.rx", k=1) or getAttr("Mery_ac_rg_thumb03.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb03.rx")
    if getAttr("Mery_ac_lf_pinky03.rx", k=1) or getAttr("Mery_ac_lf_pinky03.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky03.rx")
    if getAttr("Mery_ac_lf_pinky02.rx", k=1) or getAttr("Mery_ac_lf_pinky02.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky02.rx")
    if getAttr("Mery_ac_lf_pinky01.rx", k=1) or getAttr("Mery_ac_lf_pinky01.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky01.rx")
    if getAttr("Mery_ac_lf_pinky_base.rx", k=1) or getAttr("Mery_ac_lf_pinky_base.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky_base.rx")
    if getAttr("Mery_ac_rg_middle03.rx", k=1) or getAttr("Mery_ac_rg_middle03.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle03.rx")
    if getAttr("Mery_ac_rg_middle02.rx", k=1) or getAttr("Mery_ac_rg_middle02.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle02.rx")
    if getAttr("Mery_ac_rg_middle01.rx", k=1) or getAttr("Mery_ac_rg_middle01.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle01.rx")
    if getAttr("Mery_ac_rg_middle_base.rx", k=1) or getAttr("Mery_ac_rg_middle_base.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_middle_base.rx")
    if getAttr("Mery_ac_rg_ring03.rx", k=1) or getAttr("Mery_ac_rg_ring03.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring03.rx")
    if getAttr("Mery_ac_rg_ring02.rx", k=1) or getAttr("Mery_ac_rg_ring02.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring02.rx")
    if getAttr("Mery_ac_rg_thumb02.rx", k=1) or getAttr("Mery_ac_rg_thumb02.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb02.rx")
    if getAttr("Mery_ac_rg_thumb01.rx", k=1) or getAttr("Mery_ac_rg_thumb01.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb01.rx")
    if getAttr("Mery_ac_rg_index03.rx", k=1) or getAttr("Mery_ac_rg_index03.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_index03.rx")
    if getAttr("Mery_ac_rg_index02.rx", k=1) or getAttr("Mery_ac_rg_index02.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_index02.rx")
    if getAttr("Mery_ac_rg_index01.rx", k=1) or getAttr("Mery_ac_rg_index01.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_index01.rx")
    if getAttr("Mery_ac_rg_index_base.rx", k=1) or getAttr("Mery_ac_rg_index_base.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_index_base.rx")
    if getAttr("Mery_ac_rg_ring01.rx", k=1) or getAttr("Mery_ac_rg_ring01.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring01.rx")
    if getAttr("Mery_ac_rg_ring_base.rx", k=1) or getAttr("Mery_ac_rg_ring_base.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_ring_base.rx")
    if getAttr("Mery_ac_rg_pinky03.rx", k=1) or getAttr("Mery_ac_rg_pinky03.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky03.rx")
    if getAttr("Mery_ac_rg_pinky02.rx", k=1) or getAttr("Mery_ac_rg_pinky02.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky02.rx")
    if getAttr("Mery_ac_rg_pinky01.rx", k=1) or getAttr("Mery_ac_rg_pinky01.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky01.rx")
    if getAttr("Mery_ac_rg_pinky_base.rx", k=1) or getAttr("Mery_ac_rg_pinky_base.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky_base.rx")
    if getAttr("Mery_ac_rg_leg_control.rx", k=1) or getAttr("Mery_ac_rg_leg_control.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_leg_control.rx")
    if getAttr("Mery_ac_rg_kneePivot.rx", k=1) or getAttr("Mery_ac_rg_kneePivot.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_kneePivot.rx")
    if getAttr("Mery_ac_rg_ikfoot.rx", k=1) or getAttr("Mery_ac_rg_ikfoot.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.rx")
    if getAttr("Mery_ac_rg_toe.rx", k=1) or getAttr("Mery_ac_rg_toe.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_toe.rx")
    if getAttr("Mery_ac_lf_kneePivot.rx", k=1) or getAttr("Mery_ac_lf_kneePivot.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_kneePivot.rx")
    if getAttr("Mery_ac_lf_ikfoot.rx", k=1) or getAttr("Mery_ac_lf_ikfoot.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.rx")
    if getAttr("Mery_ac_lf_toe.rx", k=1) or getAttr("Mery_ac_lf_toe.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_toe.rx")
    if getAttr("Mery_ac_lf_leg_control.rx", k=1) or getAttr("Mery_ac_lf_leg_control.rx", channelBox=1):
        setKeyframe("Mery_ac_lf_leg_control.rx")
    if getAttr("Mery_ac_rg_arm_control.rx", k=1) or getAttr("Mery_ac_rg_arm_control.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_arm_control.rx")
    if getAttr("Mery_ac_rg_elbowPivot.rx", k=1) or getAttr("Mery_ac_rg_elbowPivot.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_elbowPivot.rx")
    if getAttr("Mery_ac_rg_ikhand.rx", k=1) or getAttr("Mery_ac_rg_ikhand.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_ikhand.rx")
    if getAttr("Mery_ac_rg_clavicle.rx", k=1) or getAttr("Mery_ac_rg_clavicle.rx", channelBox=1):
        setKeyframe("Mery_ac_rg_clavicle.rx")
    if getAttr("Mery_ac_cn_global.ry", k=1) or getAttr("Mery_ac_cn_global.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_global.ry")
    if getAttr("Mery_ac_lf_arm_control.ry", k=1) or getAttr("Mery_ac_lf_arm_control.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_arm_control.ry")
    if getAttr("Mery_ac_lf_elbowPivot.ry", k=1) or getAttr("Mery_ac_lf_elbowPivot.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_elbowPivot.ry")
    if getAttr("Mery_ac_lf_ikhand.ry", k=1) or getAttr("Mery_ac_lf_ikhand.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_ikhand.ry")
    if getAttr("Mery_ac_lf_clavicle.ry", k=1) or getAttr("Mery_ac_lf_clavicle.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_clavicle.ry")
    if getAttr("Mery_ac_cn_tongue4.ry", k=1) or getAttr("Mery_ac_cn_tongue4.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue4.ry")
    if getAttr("Mery_ac_cn_tongue3.ry", k=1) or getAttr("Mery_ac_cn_tongue3.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue3.ry")
    if getAttr("Mery_ac_cn_tongue2.ry", k=1) or getAttr("Mery_ac_cn_tongue2.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue2.ry")
    if getAttr("Mery_ac_up_teeth.ry", k=1) or getAttr("Mery_ac_up_teeth.ry", channelBox=1):
        setKeyframe("Mery_ac_up_teeth.ry")
    if getAttr("Mery_ac_cn_head.ry", k=1) or getAttr("Mery_ac_cn_head.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_head.ry")
    if getAttr("Mery_ac_cn_neck.ry", k=1) or getAttr("Mery_ac_cn_neck.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_neck.ry")
    if getAttr("Mery_ac_cn_tongue1.ry", k=1) or getAttr("Mery_ac_cn_tongue1.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue1.ry")
    if getAttr("Mery_ac_lf_eye.ry", k=1) or getAttr("Mery_ac_lf_eye.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_eye.ry")
    if getAttr("Mery_ac_rg_eye.ry", k=1) or getAttr("Mery_ac_rg_eye.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_eye.ry")
    if getAttr("Mery_ac_cn_eyes.ry", k=1) or getAttr("Mery_ac_cn_eyes.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_eyes.ry")
    if getAttr("Mery_ac_dw_teeth.ry", k=1) or getAttr("Mery_ac_dw_teeth.ry", channelBox=1):
        setKeyframe("Mery_ac_dw_teeth.ry")
    if getAttr("Mery_ac_cn_hip.ry", k=1) or getAttr("Mery_ac_cn_hip.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_hip.ry")
    if getAttr("Mery_ac_lf_breast.ry", k=1) or getAttr("Mery_ac_lf_breast.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_breast.ry")
    if getAttr("Mery_ac_rg_breast.ry", k=1) or getAttr("Mery_ac_rg_breast.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_breast.ry")
    if getAttr("Mery_ac_cn_chest.ry", k=1) or getAttr("Mery_ac_cn_chest.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_chest.ry")
    if getAttr("Mery_ac_cn_fkback02.ry", k=1) or getAttr("Mery_ac_cn_fkback02.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback02.ry")
    if getAttr("Mery_ac_cn_fkback01.ry", k=1) or getAttr("Mery_ac_cn_fkback01.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback01.ry")
    if getAttr("Mery_ac_cn_torso.ry", k=1) or getAttr("Mery_ac_cn_torso.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_torso.ry")
    if getAttr("Mery_ac_lf_index02.ry", k=1) or getAttr("Mery_ac_lf_index02.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_index02.ry")
    if getAttr("Mery_ac_lf_index01.ry", k=1) or getAttr("Mery_ac_lf_index01.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_index01.ry")
    if getAttr("Mery_ac_lf_index_base.ry", k=1) or getAttr("Mery_ac_lf_index_base.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_index_base.ry")
    if getAttr("Mery_ac_lf_middle03.ry", k=1) or getAttr("Mery_ac_lf_middle03.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_middle03.ry")
    if getAttr("Mery_ac_lf_middle02.ry", k=1) or getAttr("Mery_ac_lf_middle02.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_middle02.ry")
    if getAttr("Mery_ac_lf_middle01.ry", k=1) or getAttr("Mery_ac_lf_middle01.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_middle01.ry")
    if getAttr("Mery_ac_cn_vis.ry", k=1) or getAttr("Mery_ac_cn_vis.ry", channelBox=1):
        setKeyframe("Mery_ac_cn_vis.ry")
    if getAttr("Mery_ac_lf_hand_cup.ry", k=1) or getAttr("Mery_ac_lf_hand_cup.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_hand_cup.ry")
    if getAttr("Mery_ac_lf_thumb03.ry", k=1) or getAttr("Mery_ac_lf_thumb03.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb03.ry")
    if getAttr("Mery_ac_lf_thumb02.ry", k=1) or getAttr("Mery_ac_lf_thumb02.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb02.ry")
    if getAttr("Mery_ac_lf_thumb01.ry", k=1) or getAttr("Mery_ac_lf_thumb01.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb01.ry")
    if getAttr("Mery_ac_lf_index03.ry", k=1) or getAttr("Mery_ac_lf_index03.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_index03.ry")
    if getAttr("Mery_ac_lf_middle_base.ry", k=1) or getAttr("Mery_ac_lf_middle_base.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_middle_base.ry")
    if getAttr("Mery_ac_lf_ring03.ry", k=1) or getAttr("Mery_ac_lf_ring03.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_ring03.ry")
    if getAttr("Mery_ac_lf_ring02.ry", k=1) or getAttr("Mery_ac_lf_ring02.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_ring02.ry")
    if getAttr("Mery_ac_lf_ring01.ry", k=1) or getAttr("Mery_ac_lf_ring01.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_ring01.ry")
    if getAttr("Mery_ac_lf_ring_base.ry", k=1) or getAttr("Mery_ac_lf_ring_base.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_ring_base.ry")
    if getAttr("Mery_ac_rg_hand_cup.ry", k=1) or getAttr("Mery_ac_rg_hand_cup.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_hand_cup.ry")
    if getAttr("Mery_ac_rg_thumb03.ry", k=1) or getAttr("Mery_ac_rg_thumb03.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb03.ry")
    if getAttr("Mery_ac_lf_pinky03.ry", k=1) or getAttr("Mery_ac_lf_pinky03.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky03.ry")
    if getAttr("Mery_ac_lf_pinky02.ry", k=1) or getAttr("Mery_ac_lf_pinky02.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky02.ry")
    if getAttr("Mery_ac_lf_pinky01.ry", k=1) or getAttr("Mery_ac_lf_pinky01.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky01.ry")
    if getAttr("Mery_ac_lf_pinky_base.ry", k=1) or getAttr("Mery_ac_lf_pinky_base.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky_base.ry")
    if getAttr("Mery_ac_rg_middle03.ry", k=1) or getAttr("Mery_ac_rg_middle03.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_middle03.ry")
    if getAttr("Mery_ac_rg_middle02.ry", k=1) or getAttr("Mery_ac_rg_middle02.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_middle02.ry")
    if getAttr("Mery_ac_rg_middle01.ry", k=1) or getAttr("Mery_ac_rg_middle01.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_middle01.ry")
    if getAttr("Mery_ac_rg_middle_base.ry", k=1) or getAttr("Mery_ac_rg_middle_base.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_middle_base.ry")
    if getAttr("Mery_ac_rg_ring03.ry", k=1) or getAttr("Mery_ac_rg_ring03.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_ring03.ry")
    if getAttr("Mery_ac_rg_ring02.ry", k=1) or getAttr("Mery_ac_rg_ring02.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_ring02.ry")
    if getAttr("Mery_ac_rg_thumb02.ry", k=1) or getAttr("Mery_ac_rg_thumb02.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb02.ry")
    if getAttr("Mery_ac_rg_thumb01.ry", k=1) or getAttr("Mery_ac_rg_thumb01.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb01.ry")
    if getAttr("Mery_ac_rg_index03.ry", k=1) or getAttr("Mery_ac_rg_index03.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_index03.ry")
    if getAttr("Mery_ac_rg_index02.ry", k=1) or getAttr("Mery_ac_rg_index02.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_index02.ry")
    if getAttr("Mery_ac_rg_index01.ry", k=1) or getAttr("Mery_ac_rg_index01.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_index01.ry")
    if getAttr("Mery_ac_rg_index_base.ry", k=1) or getAttr("Mery_ac_rg_index_base.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_index_base.ry")
    if getAttr("Mery_ac_rg_ring01.ry", k=1) or getAttr("Mery_ac_rg_ring01.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_ring01.ry")
    if getAttr("Mery_ac_rg_ring_base.ry", k=1) or getAttr("Mery_ac_rg_ring_base.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_ring_base.ry")
    if getAttr("Mery_ac_rg_pinky03.ry", k=1) or getAttr("Mery_ac_rg_pinky03.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky03.ry")
    if getAttr("Mery_ac_rg_pinky02.ry", k=1) or getAttr("Mery_ac_rg_pinky02.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky02.ry")
    if getAttr("Mery_ac_rg_pinky01.ry", k=1) or getAttr("Mery_ac_rg_pinky01.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky01.ry")
    if getAttr("Mery_ac_rg_pinky_base.ry", k=1) or getAttr("Mery_ac_rg_pinky_base.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky_base.ry")
    if getAttr("Mery_ac_rg_leg_control.ry", k=1) or getAttr("Mery_ac_rg_leg_control.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_leg_control.ry")
    if getAttr("Mery_ac_rg_kneePivot.ry", k=1) or getAttr("Mery_ac_rg_kneePivot.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_kneePivot.ry")
    if getAttr("Mery_ac_rg_ikfoot.ry", k=1) or getAttr("Mery_ac_rg_ikfoot.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.ry")
    if getAttr("Mery_ac_rg_toe.ry", k=1) or getAttr("Mery_ac_rg_toe.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_toe.ry")
    if getAttr("Mery_ac_lf_kneePivot.ry", k=1) or getAttr("Mery_ac_lf_kneePivot.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_kneePivot.ry")
    if getAttr("Mery_ac_lf_ikfoot.ry", k=1) or getAttr("Mery_ac_lf_ikfoot.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.ry")
    if getAttr("Mery_ac_lf_toe.ry", k=1) or getAttr("Mery_ac_lf_toe.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_toe.ry")
    if getAttr("Mery_ac_lf_leg_control.ry", k=1) or getAttr("Mery_ac_lf_leg_control.ry", channelBox=1):
        setKeyframe("Mery_ac_lf_leg_control.ry")
    if getAttr("Mery_ac_rg_arm_control.ry", k=1) or getAttr("Mery_ac_rg_arm_control.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_arm_control.ry")
    if getAttr("Mery_ac_rg_elbowPivot.ry", k=1) or getAttr("Mery_ac_rg_elbowPivot.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_elbowPivot.ry")
    if getAttr("Mery_ac_rg_ikhand.ry", k=1) or getAttr("Mery_ac_rg_ikhand.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_ikhand.ry")
    if getAttr("Mery_ac_rg_clavicle.ry", k=1) or getAttr("Mery_ac_rg_clavicle.ry", channelBox=1):
        setKeyframe("Mery_ac_rg_clavicle.ry")
    if getAttr("Mery_ac_cn_global.rz", k=1) or getAttr("Mery_ac_cn_global.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_global.rz")
    if getAttr("Mery_ac_lf_arm_control.rz", k=1) or getAttr("Mery_ac_lf_arm_control.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_arm_control.rz")
    if getAttr("Mery_ac_lf_elbowPivot.rz", k=1) or getAttr("Mery_ac_lf_elbowPivot.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_elbowPivot.rz")
    if getAttr("Mery_ac_lf_ikhand.rz", k=1) or getAttr("Mery_ac_lf_ikhand.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_ikhand.rz")
    if getAttr("Mery_ac_lf_clavicle.rz", k=1) or getAttr("Mery_ac_lf_clavicle.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_clavicle.rz")
    if getAttr("Mery_ac_cn_tongue4.rz", k=1) or getAttr("Mery_ac_cn_tongue4.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue4.rz")
    if getAttr("Mery_ac_cn_tongue3.rz", k=1) or getAttr("Mery_ac_cn_tongue3.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue3.rz")
    if getAttr("Mery_ac_cn_tongue2.rz", k=1) or getAttr("Mery_ac_cn_tongue2.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue2.rz")
    if getAttr("Mery_ac_up_teeth.rz", k=1) or getAttr("Mery_ac_up_teeth.rz", channelBox=1):
        setKeyframe("Mery_ac_up_teeth.rz")
    if getAttr("Mery_ac_cn_head.rz", k=1) or getAttr("Mery_ac_cn_head.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_head.rz")
    if getAttr("Mery_ac_cn_neck.rz", k=1) or getAttr("Mery_ac_cn_neck.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_neck.rz")
    if getAttr("Mery_ac_cn_tongue1.rz", k=1) or getAttr("Mery_ac_cn_tongue1.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_tongue1.rz")
    if getAttr("Mery_ac_lf_eye.rz", k=1) or getAttr("Mery_ac_lf_eye.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_eye.rz")
    if getAttr("Mery_ac_rg_eye.rz", k=1) or getAttr("Mery_ac_rg_eye.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_eye.rz")
    if getAttr("Mery_ac_cn_eyes.rz", k=1) or getAttr("Mery_ac_cn_eyes.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_eyes.rz")
    if getAttr("Mery_ac_dw_teeth.rz", k=1) or getAttr("Mery_ac_dw_teeth.rz", channelBox=1):
        setKeyframe("Mery_ac_dw_teeth.rz")
    if getAttr("Mery_ac_cn_hip.rz", k=1) or getAttr("Mery_ac_cn_hip.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_hip.rz")
    if getAttr("Mery_ac_lf_breast.rz", k=1) or getAttr("Mery_ac_lf_breast.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_breast.rz")
    if getAttr("Mery_ac_rg_breast.rz", k=1) or getAttr("Mery_ac_rg_breast.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_breast.rz")
    if getAttr("Mery_ac_cn_chest.rz", k=1) or getAttr("Mery_ac_cn_chest.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_chest.rz")
    if getAttr("Mery_ac_cn_fkback02.rz", k=1) or getAttr("Mery_ac_cn_fkback02.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback02.rz")
    if getAttr("Mery_ac_cn_fkback01.rz", k=1) or getAttr("Mery_ac_cn_fkback01.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_fkback01.rz")
    if getAttr("Mery_ac_cn_torso.rz", k=1) or getAttr("Mery_ac_cn_torso.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_torso.rz")
    if getAttr("Mery_ac_lf_index02.rz", k=1) or getAttr("Mery_ac_lf_index02.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_index02.rz")
    if getAttr("Mery_ac_lf_index01.rz", k=1) or getAttr("Mery_ac_lf_index01.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_index01.rz")
    if getAttr("Mery_ac_lf_index_base.rz", k=1) or getAttr("Mery_ac_lf_index_base.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_index_base.rz")
    if getAttr("Mery_ac_lf_middle03.rz", k=1) or getAttr("Mery_ac_lf_middle03.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle03.rz")
    if getAttr("Mery_ac_lf_middle02.rz", k=1) or getAttr("Mery_ac_lf_middle02.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle02.rz")
    if getAttr("Mery_ac_lf_middle01.rz", k=1) or getAttr("Mery_ac_lf_middle01.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle01.rz")
    if getAttr("Mery_ac_cn_vis.rz", k=1) or getAttr("Mery_ac_cn_vis.rz", channelBox=1):
        setKeyframe("Mery_ac_cn_vis.rz")
    if getAttr("Mery_ac_lf_hand_cup.rz", k=1) or getAttr("Mery_ac_lf_hand_cup.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_hand_cup.rz")
    if getAttr("Mery_ac_lf_thumb03.rz", k=1) or getAttr("Mery_ac_lf_thumb03.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb03.rz")
    if getAttr("Mery_ac_lf_thumb02.rz", k=1) or getAttr("Mery_ac_lf_thumb02.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb02.rz")
    if getAttr("Mery_ac_lf_thumb01.rz", k=1) or getAttr("Mery_ac_lf_thumb01.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_thumb01.rz")
    if getAttr("Mery_ac_lf_index03.rz", k=1) or getAttr("Mery_ac_lf_index03.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_index03.rz")
    if getAttr("Mery_ac_lf_middle_base.rz", k=1) or getAttr("Mery_ac_lf_middle_base.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_middle_base.rz")
    if getAttr("Mery_ac_lf_ring03.rz", k=1) or getAttr("Mery_ac_lf_ring03.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring03.rz")
    if getAttr("Mery_ac_lf_ring02.rz", k=1) or getAttr("Mery_ac_lf_ring02.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring02.rz")
    if getAttr("Mery_ac_lf_ring01.rz", k=1) or getAttr("Mery_ac_lf_ring01.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring01.rz")
    if getAttr("Mery_ac_lf_ring_base.rz", k=1) or getAttr("Mery_ac_lf_ring_base.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_ring_base.rz")
    if getAttr("Mery_ac_rg_hand_cup.rz", k=1) or getAttr("Mery_ac_rg_hand_cup.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_hand_cup.rz")
    if getAttr("Mery_ac_rg_thumb03.rz", k=1) or getAttr("Mery_ac_rg_thumb03.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb03.rz")
    if getAttr("Mery_ac_lf_pinky03.rz", k=1) or getAttr("Mery_ac_lf_pinky03.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky03.rz")
    if getAttr("Mery_ac_lf_pinky02.rz", k=1) or getAttr("Mery_ac_lf_pinky02.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky02.rz")
    if getAttr("Mery_ac_lf_pinky01.rz", k=1) or getAttr("Mery_ac_lf_pinky01.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky01.rz")
    if getAttr("Mery_ac_lf_pinky_base.rz", k=1) or getAttr("Mery_ac_lf_pinky_base.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_pinky_base.rz")
    if getAttr("Mery_ac_rg_middle03.rz", k=1) or getAttr("Mery_ac_rg_middle03.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle03.rz")
    if getAttr("Mery_ac_rg_middle02.rz", k=1) or getAttr("Mery_ac_rg_middle02.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle02.rz")
    if getAttr("Mery_ac_rg_middle01.rz", k=1) or getAttr("Mery_ac_rg_middle01.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle01.rz")
    if getAttr("Mery_ac_rg_middle_base.rz", k=1) or getAttr("Mery_ac_rg_middle_base.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_middle_base.rz")
    if getAttr("Mery_ac_rg_ring03.rz", k=1) or getAttr("Mery_ac_rg_ring03.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring03.rz")
    if getAttr("Mery_ac_rg_ring02.rz", k=1) or getAttr("Mery_ac_rg_ring02.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring02.rz")
    if getAttr("Mery_ac_rg_thumb02.rz", k=1) or getAttr("Mery_ac_rg_thumb02.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb02.rz")
    if getAttr("Mery_ac_rg_thumb01.rz", k=1) or getAttr("Mery_ac_rg_thumb01.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_thumb01.rz")
    if getAttr("Mery_ac_rg_index03.rz", k=1) or getAttr("Mery_ac_rg_index03.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_index03.rz")
    if getAttr("Mery_ac_rg_index02.rz", k=1) or getAttr("Mery_ac_rg_index02.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_index02.rz")
    if getAttr("Mery_ac_rg_index01.rz", k=1) or getAttr("Mery_ac_rg_index01.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_index01.rz")
    if getAttr("Mery_ac_rg_index_base.rz", k=1) or getAttr("Mery_ac_rg_index_base.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_index_base.rz")
    if getAttr("Mery_ac_rg_ring01.rz", k=1) or getAttr("Mery_ac_rg_ring01.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring01.rz")
    if getAttr("Mery_ac_rg_ring_base.rz", k=1) or getAttr("Mery_ac_rg_ring_base.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_ring_base.rz")
    if getAttr("Mery_ac_rg_pinky03.rz", k=1) or getAttr("Mery_ac_rg_pinky03.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky03.rz")
    if getAttr("Mery_ac_rg_pinky02.rz", k=1) or getAttr("Mery_ac_rg_pinky02.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky02.rz")
    if getAttr("Mery_ac_rg_pinky01.rz", k=1) or getAttr("Mery_ac_rg_pinky01.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky01.rz")
    if getAttr("Mery_ac_rg_pinky_base.rz", k=1) or getAttr("Mery_ac_rg_pinky_base.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_pinky_base.rz")
    if getAttr("Mery_ac_rg_leg_control.rz", k=1) or getAttr("Mery_ac_rg_leg_control.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_leg_control.rz")
    if getAttr("Mery_ac_rg_kneePivot.rz", k=1) or getAttr("Mery_ac_rg_kneePivot.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_kneePivot.rz")
    if getAttr("Mery_ac_rg_ikfoot.rz", k=1) or getAttr("Mery_ac_rg_ikfoot.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.rz")
    if getAttr("Mery_ac_rg_toe.rz", k=1) or getAttr("Mery_ac_rg_toe.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_toe.rz")
    if getAttr("Mery_ac_lf_kneePivot.rz", k=1) or getAttr("Mery_ac_lf_kneePivot.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_kneePivot.rz")
    if getAttr("Mery_ac_lf_ikfoot.rz", k=1) or getAttr("Mery_ac_lf_ikfoot.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.rz")
    if getAttr("Mery_ac_lf_toe.rz", k=1) or getAttr("Mery_ac_lf_toe.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_toe.rz")
    if getAttr("Mery_ac_lf_leg_control.rz", k=1) or getAttr("Mery_ac_lf_leg_control.rz", channelBox=1):
        setKeyframe("Mery_ac_lf_leg_control.rz")
    if getAttr("Mery_ac_rg_arm_control.rz", k=1) or getAttr("Mery_ac_rg_arm_control.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_arm_control.rz")
    if getAttr("Mery_ac_rg_elbowPivot.rz", k=1) or getAttr("Mery_ac_rg_elbowPivot.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_elbowPivot.rz")
    if getAttr("Mery_ac_rg_ikhand.rz", k=1) or getAttr("Mery_ac_rg_ikhand.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_ikhand.rz")
    if getAttr("Mery_ac_rg_clavicle.rz", k=1) or getAttr("Mery_ac_rg_clavicle.rz", channelBox=1):
        setKeyframe("Mery_ac_rg_clavicle.rz")
    if getAttr("Mery_ac_rg_ikfoot.ball_lift", k=1) or getAttr("Mery_ac_rg_ikfoot.ball_lift", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.ball_lift")
    if getAttr("Mery_ac_lf_ikfoot.ball_lift", k=1) or getAttr("Mery_ac_lf_ikfoot.ball_lift", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.ball_lift")
    if getAttr("Mery_ac_rg_ikfoot.toe_lift", k=1) or getAttr("Mery_ac_rg_ikfoot.toe_lift", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.toe_lift")
    if getAttr("Mery_ac_lf_ikfoot.toe_lift", k=1) or getAttr("Mery_ac_lf_ikfoot.toe_lift", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.toe_lift")
    if getAttr("Mery_ac_rg_ikfoot.heel_lift", k=1) or getAttr("Mery_ac_rg_ikfoot.heel_lift", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.heel_lift")
    if getAttr("Mery_ac_lf_ikfoot.heel_lift", k=1) or getAttr("Mery_ac_lf_ikfoot.heel_lift", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.heel_lift")
    if getAttr("Mery_ac_rg_ikfoot.lean", k=1) or getAttr("Mery_ac_rg_ikfoot.lean", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.lean")
    if getAttr("Mery_ac_lf_ikfoot.lean", k=1) or getAttr("Mery_ac_lf_ikfoot.lean", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.lean")
    if getAttr("Mery_ac_rg_ikfoot.side", k=1) or getAttr("Mery_ac_rg_ikfoot.side", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.side")
    if getAttr("Mery_ac_lf_ikfoot.side", k=1) or getAttr("Mery_ac_lf_ikfoot.side", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.side")
    if getAttr("Mery_ac_rg_ikfoot.heel_spin", k=1) or getAttr("Mery_ac_rg_ikfoot.heel_spin", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.heel_spin")
    if getAttr("Mery_ac_lf_ikfoot.heel_spin", k=1) or getAttr("Mery_ac_lf_ikfoot.heel_spin", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.heel_spin")
    if getAttr("Mery_ac_rg_ikfoot.toe_spin", k=1) or getAttr("Mery_ac_rg_ikfoot.toe_spin", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.toe_spin")
    if getAttr("Mery_ac_lf_ikfoot.toe_spin", k=1) or getAttr("Mery_ac_lf_ikfoot.toe_spin", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.toe_spin")
    if getAttr("Mery_ac_rg_ikfoot.stretchy", k=1) or getAttr("Mery_ac_rg_ikfoot.stretchy", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.stretchy")
    if getAttr("Mery_ac_lf_ikfoot.stretchy", k=1) or getAttr("Mery_ac_lf_ikfoot.stretchy", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.stretchy")
    if getAttr("Mery_ac_rg_ikfoot.ball_lift", k=1) or getAttr("Mery_ac_rg_ikfoot.ball_lift", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.ball_lift")
    if getAttr("Mery_ac_lf_ikfoot.ball_lift", k=1) or getAttr("Mery_ac_lf_ikfoot.ball_lift", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.ball_lift")
    if getAttr("Mery_ac_rg_ikfoot.toe_lift", k=1) or getAttr("Mery_ac_rg_ikfoot.toe_lift", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.toe_lift")
    if getAttr("Mery_ac_lf_ikfoot.toe_lift", k=1) or getAttr("Mery_ac_lf_ikfoot.toe_lift", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.toe_lift")
    if getAttr("Mery_ac_rg_ikfoot.heel_lift", k=1) or getAttr("Mery_ac_rg_ikfoot.heel_lift", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.heel_lift")
    if getAttr("Mery_ac_lf_ikfoot.heel_lift", k=1) or getAttr("Mery_ac_lf_ikfoot.heel_lift", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.heel_lift")
    if getAttr("Mery_ac_rg_ikfoot.lean", k=1) or getAttr("Mery_ac_rg_ikfoot.lean", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.lean")
    if getAttr("Mery_ac_lf_ikfoot.lean", k=1) or getAttr("Mery_ac_lf_ikfoot.lean", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.lean")
    if getAttr("Mery_ac_rg_ikfoot.side", k=1) or getAttr("Mery_ac_rg_ikfoot.side", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.side")
    if getAttr("Mery_ac_lf_ikfoot.side", k=1) or getAttr("Mery_ac_lf_ikfoot.side", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.side")
    if getAttr("Mery_ac_rg_ikfoot.heel_spin", k=1) or getAttr("Mery_ac_rg_ikfoot.heel_spin", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.heel_spin")
    if getAttr("Mery_ac_lf_ikfoot.heel_spin", k=1) or getAttr("Mery_ac_lf_ikfoot.heel_spin", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.heel_spin")
    if getAttr("Mery_ac_rg_ikfoot.toe_spin", k=1) or getAttr("Mery_ac_rg_ikfoot.toe_spin", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.toe_spin")
    if getAttr("Mery_ac_lf_ikfoot.toe_spin", k=1) or getAttr("Mery_ac_lf_ikfoot.toe_spin", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.toe_spin")
    if getAttr("Mery_ac_rg_ikfoot.stretchy", k=1) or getAttr("Mery_ac_rg_ikfoot.stretchy", channelBox=1):
        setKeyframe("Mery_ac_rg_ikfoot.stretchy")
    if getAttr("Mery_ac_lf_ikfoot.stretchy", k=1) or getAttr("Mery_ac_lf_ikfoot.stretchy", channelBox=1):
        setKeyframe("Mery_ac_lf_ikfoot.stretchy")
