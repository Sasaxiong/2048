#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build unified prototype HTML: insert P1, P2, P7 page views into account-config-prototypes.html
"""

with open('/workspace/account-config-prototypes.html', 'r', encoding='utf-8') as f:
    src = f.read()

P1_PAGE = '''
<!-- ================================================================
     P1: 业务类型配置
================================================================ -->
<div class="page-view" id="p1">
  <div class="card"><div class="card-body">
    <div class="page-title">业务类型配置
      <button class="btn btn-success" onclick="showModal('m1-add')">+ 新增业务类型</button>
    </div>
    <div class="filter">
      <div class="filter-item"><label>业务类型名称：</label><input class="filter-input" placeholder="请输入业务类型名称"></div>
      <div class="filter-item"><label>业务类型ID：</label><input class="filter-input" placeholder="请输入业务类型ID"></div>
      <div class="filter-item"><label>审核状态：</label>
        <select class="filter-select" style="width:120px"><option>全部</option><option>待审核</option><option>审核通过</option><option>审核拒绝</option></select>
      </div>
      <div class="filter-btns"><button class="btn btn-primary">查询</button><button class="btn btn-default">重置</button></div>
    </div>
    <table>
      <thead><tr>
        <th>业务类型名称</th><th>业务类型简称</th><th>业务类型ID</th><th>审核状态</th>
        <th>启用状态</th><th>创建时间</th><th>更新时间</th><th>创建人</th><th>审核人</th><th>操作</th>
      </tr></thead>
      <tbody>
        <tr class="sys">
          <td>Acquiring <span class="tag-sys">系统初始化</span></td><td>ACQ</td><td>ACQ</td>
          <td><span class="tag tag-pass">审核通过</span></td>
          <td><label class="switch"><input type="checkbox" checked disabled><span class="slider"></span></label></td>
          <td>2026/04/11 19:02</td><td>2026/04/11 19:02</td><td>系统自动创建</td><td>系统管理员</td>
          <td><button class="btn-text" onclick="showModal(\'m1-detail\')">详情</button></td>
        </tr>
        <tr>
          <td>KBA</td><td>KBA</td><td>KBA</td>
          <td><span class="tag tag-wait">待审核</span></td>
          <td><label class="switch"><input type="checkbox"><span class="slider"></span></label></td>
          <td>2026/04/11 19:02</td><td>2026/04/11 19:02</td><td>Sasa</td><td>-</td>
          <td>
            <button class="btn-text" onclick="showModal(\'m1-audit\')">审核</button>
            <button class="btn-text" onclick="showModal(\'m1-edit\')">编辑</button>
            <button class="btn-text" onclick="showModal(\'m1-detail\')">详情</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <div>每页显示：<select><option>10</option><option>20</option></select> 条</div>
      <div>共 2 条</div>
      <div class="pages"><span>上一页</span><span class="active">1</span><span>下一页</span></div>
    </div>
  </div></div>
</div>
'''

P2_PAGE = '''
<!-- ================================================================
     P2: 账户实体配置
================================================================ -->
<div class="page-view" id="p2">
  <div class="card"><div class="card-body">
    <div class="page-title">账户实体配置
      <button class="btn btn-success" onclick="showModal(\'m2-add\')">+ 新增实体类型</button>
    </div>
    <div class="filter">
      <div class="filter-item"><label>业务类型ID：</label>
        <select class="filter-select"><option>全部</option><option>ACQ（收单）</option><option>KBA</option></select>
      </div>
      <div class="filter-item"><label>实体类型名称：</label><input class="filter-input" placeholder="请输入实体类型名称"></div>
      <div class="filter-btns"><button class="btn btn-primary">查询</button><button class="btn btn-default">重置</button></div>
    </div>
    <table>
      <thead><tr>
        <th>业务类型ID</th><th>英文实体名称</th><th>英文简称</th><th>实体类型ID</th>
        <th>实体大类</th><th>层级深度</th><th>默认子账户组</th><th>分户账</th>
        <th>审核状态</th><th>启用状态</th><th>创建时间</th><th>创建人</th><th>审核人</th><th>操作</th>
      </tr></thead>
      <tbody>
        <tr class="sys"><td>ACQ</td><td>KPay <span class="tag-sys">系统初始化</span></td><td>KPAY</td><td>JP_ACQ_KPAY</td>
          <td>自有公司</td><td>L1</td><td>-</td><td>开通</td>
          <td><span class="tag tag-pass">审核通过</span></td>
          <td><label class="switch"><input type="checkbox" checked disabled><span class="slider"></span></label></td>
          <td>2026/04/11 19:00</td><td>系统</td><td>系统</td>
          <td><button class="btn-text" onclick="showModal(\'m2-detail\')">详情</button></td>
        </tr>
        <tr class="sys"><td>ACQ</td><td>Channel <span class="tag-sys">系统初始化</span></td><td>CHANNEL</td><td>JP_ACQ_CHANNEL</td>
          <td>上游通道</td><td>L2</td><td>-</td><td>开通</td>
          <td><span class="tag tag-pass">审核通过</span></td>
          <td><label class="switch"><input type="checkbox" checked disabled><span class="slider"></span></label></td>
          <td>2026/04/11 19:00</td><td>系统</td><td>系统</td>
          <td><button class="btn-text" onclick="showModal(\'m2-detail\')">详情</button></td>
        </tr>
        <tr class="sys"><td>ACQ</td><td>Merchant <span class="tag-sys">系统初始化</span></td><td>MERCHANT</td><td>JP_ACQ_MERCHANT</td>
          <td>下游机构/代理</td><td>L4</td><td>交易, 待结算, 可提现...</td><td>开通</td>
          <td><span class="tag tag-pass">审核通过</span></td>
          <td><label class="switch"><input type="checkbox" checked disabled><span class="slider"></span></label></td>
          <td>2026/04/11 19:00</td><td>系统</td><td>系统</td>
          <td><button class="btn-text" onclick="showModal(\'m2-detail\')">详情</button></td>
        </tr>
        <tr class="sys"><td>ACQ</td><td>Store <span class="tag-sys">系统初始化</span></td><td>STORE</td><td>JP_ACQ_STORE</td>
          <td>下游机构/代理</td><td>L5</td><td>-</td><td>开通</td>
          <td><span class="tag tag-pass">审核通过</span></td>
          <td><label class="switch"><input type="checkbox" checked disabled><span class="slider"></span></label></td>
          <td>2026/04/11 19:00</td><td>系统</td><td>系统</td>
          <td><button class="btn-text" onclick="showModal(\'m2-detail\')">详情</button></td>
        </tr>
        <tr>
          <td>ACQ</td><td>Agent</td><td>AGENT</td><td>JP_ACQ_AGENT</td>
          <td>下游机构/代理</td><td>L3</td><td>-</td><td>开通</td>
          <td><span class="tag tag-wait">待审核</span></td>
          <td><label class="switch"><input type="checkbox"><span class="slider"></span></label></td>
          <td>2026/04/18 10:00</td><td>Sasa</td><td>-</td>
          <td>
            <button class="btn-text" onclick="showModal(\'m2-audit\')">审核</button>
            <button class="btn-text" onclick="showModal(\'m2-edit\')">编辑</button>
            <button class="btn-text" onclick="showModal(\'m2-detail\')">详情</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <div>共 5 条</div>
      <div class="pages"><span>上一页</span><span class="active">1</span><span>下一页</span></div>
    </div>
  </div></div>
</div>
'''

P7_PAGE = '''
<!-- ================================================================
     P7: 业务场景配置
================================================================ -->
<div class="page-view" id="p7">
  <div class="card"><div class="card-body">
    <div class="page-title">业务场景配置
      <button class="btn btn-success" onclick="showModal(\'m7-add\')">+ 新增业务场景</button>
    </div>
    <div class="filter">
      <div class="filter-item"><label>业务场景名称：</label><input class="filter-input" placeholder="请输入业务场景名称"></div>
      <div class="filter-item"><label>场景大类：</label>
        <select class="filter-select" style="width:100px"><option>全部</option><option>交易</option><option>对账</option><option>结算</option><option>出款</option></select>
      </div>
      <div class="filter-item"><label>审核状态：</label>
        <select class="filter-select" style="width:120px"><option>全部</option><option>待审核</option><option>审核通过</option></select>
      </div>
      <div class="filter-btns"><button class="btn btn-primary">查询</button><button class="btn btn-default">重置</button></div>
    </div>
    <table>
      <thead><tr>
        <th>业务场景名称</th><th>业务场景简称</th><th>业务场景ID</th><th>场景大类</th>
        <th>审核状态</th><th>启用状态</th><th>创建时间</th><th>创建人</th><th>审核人</th><th>操作</th>
      </tr></thead>
      <tbody>
        <tr class="sys">
          <td>SALE <span class="tag-sys">系统初始化</span></td><td>SALE</td><td>SCE_SALE</td><td>交易</td>
          <td><span class="tag tag-pass">审核通过</span></td>
          <td><label class="switch"><input type="checkbox" checked disabled><span class="slider"></span></label></td>
          <td>2026/04/11 19:00</td><td>系统</td><td>系统</td>
          <td><button class="btn-text" onclick="showModal(\'m7-detail\')">详情</button></td>
        </tr>
        <tr>
          <td>REFUND</td><td>REF</td><td>SCE_REFUND</td><td>交易</td>
          <td><span class="tag tag-wait">待审核</span></td>
          <td><label class="switch"><input type="checkbox"><span class="slider"></span></label></td>
          <td>2026/04/23 11:00</td><td>Sasa</td><td>-</td>
          <td>
            <button class="btn-text" onclick="showModal(\'m7-audit\')">审核</button>
            <button class="btn-text" onclick="showModal(\'m7-edit\')">编辑</button>
            <button class="btn-text" onclick="showModal(\'m7-detail\')">详情</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <div>共 2 条</div>
      <div class="pages"><span>上一页</span><span class="active">1</span><span>下一页</span></div>
    </div>
  </div></div>
</div>
'''

P1_MODALS = '''
<!-- ===== M1: 业务类型 新增 ===== -->
<div class="modal" id="m1-add">
  <div class="modal-dialog" style="width:640px">
    <div class="modal-header"><h3>新增业务类型</h3><button class="close-btn" onclick="hideModal(\'m1-add\')">×</button></div>
    <div class="modal-body">
      <div class="form-item"><label class="form-label"><span class="req">*</span>业务类型名称</label>
        <div class="form-content">
          <input class="form-input" placeholder="请输入业务类型名称">
          <div class="form-tip">仅允许英文字母、数字、下划线、空格、点（.）；首尾不能为空格</div>
        </div>
      </div>
      <div class="form-item"><label class="form-label"><span class="req">*</span>业务类型简称</label>
        <div class="form-content">
          <input class="form-input" placeholder="请输入业务类型简称">
          <div class="form-tip">仅允许15字符以内，英文字母、数字、空格、点、连字符、撇号、&符号</div>
        </div>
      </div>
      <div class="form-item"><label class="form-label"><span class="req">*</span>业务类型ID</label>
        <div class="form-content">
          <input class="form-input" placeholder="请输入业务类型ID">
          <div class="form-tip">仅允许50字符以内，保存后不可修改</div>
        </div>
      </div>
      <div class="form-item"><label class="form-label">启用状态</label>
        <div class="form-content" style="padding-top:7px"><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div>
      </div>
      <div class="form-item"><label class="form-label"><span class="req">*</span>审核通过启用状态</label>
        <div class="form-content">
          <div class="radio-group">
            <label><input type="radio" name="m1en" checked> 自动启用</label>
            <label><input type="radio" name="m1en"> 手动启用</label>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-footer between">
      <button class="btn btn-default" onclick="hideModal(\'m1-add\')">取消</button>
      <button class="btn btn-primary">提交审核</button>
    </div>
  </div>
</div>

<!-- ===== M1: 编辑 ===== -->
<div class="modal" id="m1-edit">
  <div class="modal-dialog" style="width:640px">
    <div class="modal-header"><h3>编辑业务类型 — KBA</h3><button class="close-btn" onclick="hideModal(\'m1-edit\')">×</button></div>
    <div class="modal-body">
      <div class="form-item"><label class="form-label"><span class="req">*</span>业务类型名称</label>
        <div class="form-content"><input class="form-input" value="KBA"></div>
      </div>
      <div class="form-item"><label class="form-label"><span class="req">*</span>业务类型简称</label>
        <div class="form-content"><input class="form-input" value="KBA" disabled><div class="form-tip">保存后不可修改</div></div>
      </div>
      <div class="form-item"><label class="form-label"><span class="req">*</span>业务类型ID</label>
        <div class="form-content"><input class="form-input" value="KBA" disabled><div class="form-tip">保存后不可修改</div></div>
      </div>
      <div class="form-item"><label class="form-label">启用状态</label>
        <div class="form-content" style="padding-top:7px"><label class="switch"><input type="checkbox"><span class="slider"></span></label></div>
      </div>
    </div>
    <div class="modal-footer between">
      <button class="btn btn-default" onclick="hideModal(\'m1-edit\')">取消</button>
      <button class="btn btn-primary">提交审核</button>
    </div>
  </div>
</div>

<!-- ===== M1: 新增审核 ===== -->
<div class="modal" id="m1-audit">
  <div class="modal-dialog" style="width:480px">
    <div class="modal-header"><h3>审核业务类型 — KBA</h3><button class="close-btn" onclick="hideModal(\'m1-audit\')">×</button></div>
    <div class="modal-body">
      <div class="confirm-box"><h4>您确定要审核通过 "KBA" 吗？</h4><p>业务类型ID：KBA &nbsp;&nbsp; 创建人：Sasa</p></div>
      <div class="section-title" style="margin-top:0">待审核信息</div>
      <div class="detail-row">
        <div class="detail-item"><div class="detail-label">业务类型名称</div><div class="detail-value">KBA</div></div>
        <div class="detail-item"><div class="detail-label">业务类型简称</div><div class="detail-value">KBA</div></div>
        <div class="detail-item"><div class="detail-label">业务类型ID</div><div class="detail-value">KBA</div></div>
        <div class="detail-item"><div class="detail-label">审核通过启用</div><div class="detail-value">自动启用</div></div>
      </div>
      <div class="form-item"><label class="form-label" style="width:auto;padding-right:8px">审核意见（选填）</label>
        <div class="form-content"><textarea class="form-textarea" placeholder="请输入审核意见，最大200字符"></textarea></div>
      </div>
    </div>
    <div class="modal-footer center">
      <button class="btn btn-danger">拒绝</button>
      <button class="btn btn-default" onclick="hideModal(\'m1-audit\')">取消</button>
      <button class="btn btn-primary">通过</button>
    </div>
  </div>
</div>

<!-- ===== M1: 编辑审核（对比） ===== -->
<div class="modal" id="m1-edit-audit">
  <div class="modal-dialog" style="width:680px">
    <div class="modal-header"><h3>审核编辑后的业务类型 — Acquiring</h3><button class="close-btn" onclick="hideModal(\'m1-edit-audit\')">×</button></div>
    <div class="modal-body">
      <div class="compare-box">
        <div class="compare-panel">
          <div class="compare-title">修改前</div>
          <div class="compare-row"><div class="compare-label">业务类型名称</div><div class="compare-value">Acquiring</div></div>
          <div class="compare-row"><div class="compare-label">业务类型简称</div><div class="compare-value">ACQ</div></div>
          <div class="compare-row"><div class="compare-label">业务类型ID</div><div class="compare-value">ACQ</div></div>
        </div>
        <div class="compare-panel">
          <div class="compare-title">修改后</div>
          <div class="compare-row"><div class="compare-label">业务类型名称</div><div class="compare-value">Acquiring Updated</div></div>
          <div class="compare-row"><div class="compare-label">业务类型简称</div><div class="compare-value diff">ACQ_NEW <span class="diff-tag">变更</span></div></div>
          <div class="compare-row"><div class="compare-label">业务类型ID</div><div class="compare-value">ACQ</div></div>
        </div>
      </div>
      <div class="form-item"><label class="form-label" style="width:auto;padding-right:8px">审核意见（选填）</label>
        <div class="form-content"><textarea class="form-textarea" placeholder="请输入审核意见"></textarea></div>
      </div>
    </div>
    <div class="modal-footer center">
      <button class="btn btn-default">拒绝</button>
      <button class="btn btn-default" onclick="hideModal(\'m1-edit-audit\')">取消</button>
      <button class="btn btn-primary">通过</button>
    </div>
  </div>
</div>

<!-- ===== M1: 详情 ===== -->
<div class="modal" id="m1-detail">
  <div class="modal-dialog" style="width:520px">
    <div class="modal-header"><h3>业务类型详情 — Acquiring</h3><button class="close-btn" onclick="hideModal(\'m1-detail\')">×</button></div>
    <div class="modal-body">
      <div class="detail-row">
        <div class="detail-item"><div class="detail-label">业务类型ID</div><div class="detail-value">ACQ</div></div>
        <div class="detail-item"><div class="detail-label">业务类型名称</div><div class="detail-value">Acquiring</div></div>
        <div class="detail-item"><div class="detail-label">业务类型简称</div><div class="detail-value">ACQ</div></div>
        <div class="detail-item"><div class="detail-label">审核状态</div><div class="detail-value"><span class="tag tag-pass">审核通过</span></div></div>
        <div class="detail-item"><div class="detail-label">启用状态</div><div class="detail-value">启用</div></div>
        <div class="detail-item"><div class="detail-label">创建人</div><div class="detail-value">系统自动创建</div></div>
        <div class="detail-item"><div class="detail-label">创建时间</div><div class="detail-value">2026/04/11 19:02:00</div></div>
        <div class="detail-item"><div class="detail-label">审核人</div><div class="detail-value">系统管理员</div></div>
      </div>
      <div style="font-weight:600;margin-bottom:8px;font-size:13px">操作记录</div>
      <div class="timeline">
        <div class="tl-item"><div class="tl-time">2026-04-11 19:02</div><div class="tl-text">系统自动创建业务类型</div></div>
        <div class="tl-item"><div class="tl-time">2026-04-11 19:02</div><div class="tl-text">系统管理员审核通过</div></div>
      </div>
    </div>
    <div class="modal-footer right"><button class="btn btn-primary" onclick="hideModal(\'m1-detail\')">关闭</button></div>
  </div>
</div>
'''

P2_MODALS = '''
<!-- ===== M2: 账户实体 新增 ===== -->
<div class="modal" id="m2-add">
  <div class="modal-dialog" style="width:900px">
    <div class="modal-header"><h3>新增实体类型</h3><button class="close-btn" onclick="hideModal(\'m2-add\')">×</button></div>
    <div class="modal-body">
      <div class="form-row form-row-2">
        <div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>业务类型ID</label>
            <div class="form-content"><select class="form-select"><option>ACQ（收单）</option><option>KBA</option></select></div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>英文实体类型名称</label>
            <div class="form-content"><input class="form-input" placeholder="请输入英文实体类型名称">
              <div class="form-tip">仅允许英文字母、数字、下划线、空格、点(.)</div>
            </div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>英文实体类型简称</label>
            <div class="form-content"><input class="form-input" placeholder="请输入英文大写简称（最多15字符）"></div>
          </div>
          <div class="form-item"><label class="form-label">实体类型ID</label>
            <div class="form-content"><input class="form-input" disabled value="系统自动生成">
              <div class="form-tip">格式：{国家码}_{业务类型ID}_{实体简称}，例：JP_ACQ_MERCHANT</div>
            </div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>实体大类</label>
            <div class="form-content"><select class="form-select">
              <option>自有公司</option><option>上游通道</option><option>下游机构/代理</option><option>平台</option><option>客户</option>
            </select></div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>层级深度</label>
            <div class="form-content"><select class="form-select">
              <option>L1</option><option>L2</option><option>L3</option><option>L4</option><option>L5</option>
            </select></div>
          </div>
        </div>
        <div>
          <div class="form-item"><label class="form-label">允许父级实体类型</label>
            <div class="form-content">
              <div class="tag-group" id="m2-parent-tags">
                <div class="tag-item">JP_ACQ_KPAY <span onclick="this.parentElement.remove()">✕</span></div>
              </div>
              <button class="btn btn-default btn-sm" style="margin-top:6px">+ 添加父级</button>
            </div>
          </div>
          <div class="form-item"><label class="form-label">默认子账户组</label>
            <div class="form-content">
              <div class="tag-group">
                <div class="tag-item">KPay交易户 <span onclick="this.parentElement.remove()">✕</span></div>
                <div class="tag-item">KPay待结算户 <span onclick="this.parentElement.remove()">✕</span></div>
              </div>
              <button class="btn btn-default btn-sm" style="margin-top:6px">+ 添加</button>
              <div class="form-tip blue">💡 审核通过后，已选中的选项不可删除，只能新增</div>
            </div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>分户账</label>
            <div class="form-content"><select class="form-select"><option>开通</option><option>不开通</option></select></div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>审核通过启用状态</label>
            <div class="form-content">
              <div class="radio-group">
                <label><input type="radio" name="m2en" checked> 自动启用</label>
                <label><input type="radio" name="m2en"> 手动启用</label>
                <label><input type="radio" name="m2en"> 定时启用</label>
              </div>
            </div>
          </div>
          <div class="form-item"><label class="form-label">启用状态</label>
            <div class="form-content" style="padding-top:7px"><label class="switch"><input type="checkbox" checked><span class="slider"></span></label></div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-footer between">
      <button class="btn btn-default" onclick="hideModal(\'m2-add\')">取消</button>
      <button class="btn btn-primary">提交审核</button>
    </div>
  </div>
</div>

<!-- ===== M2: 编辑 ===== -->
<div class="modal" id="m2-edit">
  <div class="modal-dialog" style="width:900px">
    <div class="modal-header"><h3>编辑实体类型 — Agent</h3><button class="close-btn" onclick="hideModal(\'m2-edit\')">×</button></div>
    <div class="modal-body">
      <div class="form-row form-row-2">
        <div>
          <div class="form-item"><label class="form-label">业务类型ID</label>
            <div class="form-content"><input class="form-input" value="ACQ" disabled></div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>英文实体类型名称</label>
            <div class="form-content"><input class="form-input" value="Agent"></div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>英文实体类型简称</label>
            <div class="form-content"><input class="form-input" value="AGENT" disabled><div class="form-tip">保存后不可修改</div></div>
          </div>
          <div class="form-item"><label class="form-label">实体类型ID</label>
            <div class="form-content"><input class="form-input" disabled value="JP_ACQ_AGENT"></div>
          </div>
          <div class="form-item"><label class="form-label"><span class="req">*</span>实体大类</label>
            <div class="form-content"><select class="form-select"><option selected>下游机构/代理</option></select></div>
          </div>
        </div>
        <div>
          <div class="form-item"><label class="form-label">允许父级</label>
            <div class="form-content">
              <div class="tag-group"><div class="tag-item">JP_ACQ_KPAY <span>✕</span></div></div>
              <button class="btn btn-default btn-sm" style="margin-top:6px">+ 添加父级</button>
            </div>
          </div>
          <div class="form-item"><label class="form-label">默认子账户组</label>
            <div class="form-content">
              <div class="tag-group"><div class="tag-item">KPay分润户 <span>✕</span></div></div>
              <button class="btn btn-default btn-sm" style="margin-top:6px">+ 添加</button>
              <div class="form-tip blue">💡 已审核通过的选项不可删除，只能新增</div>
            </div>
          </div>
          <div class="form-item"><label class="form-label">分户账</label>
            <div class="form-content"><select class="form-select"><option>开通</option></select></div>
          </div>
          <div class="form-item"><label class="form-label">启用状态</label>
            <div class="form-content" style="padding-top:7px"><label class="switch"><input type="checkbox"><span class="slider"></span></label></div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-footer between">
      <button class="btn btn-default" onclick="hideModal(\'m2-edit\')">取消</button>
      <button class="btn btn-primary">提交审核</button>
    </div>
  </div>
</div>

<!-- ===== M2: 新增审核 ===== -->
<div class="modal" id="m2-audit">
  <div class="modal-dialog" style="width:560px">
    <div class="modal-header"><h3>审核实体类型 — Agent</h3><button class="close-btn" onclick="hideModal(\'m2-audit\')">×</button></div>
    <div class="modal-body">
      <div class="confirm-box"><h4>您确定要审核通过 "Agent" 吗？</h4><p>实体类型ID：JP_ACQ_AGENT &nbsp;&nbsp; 创建人：Sasa</p></div>
      <div class="section-title" style="margin-top:0">待审核信息</div>
      <div class="detail-row">
        <div class="detail-item"><div class="detail-label">英文实体类型名称</div><div class="detail-value">Agent</div></div>
        <div class="detail-item"><div class="detail-label">英文实体类型简称</div><div class="detail-value">AGENT</div></div>
        <div class="detail-item"><div class="detail-label">实体类型ID</div><div class="detail-value">JP_ACQ_AGENT</div></div>
        <div class="detail-item"><div class="detail-label">实体大类</div><div class="detail-value">下游机构/代理</div></div>
        <div class="detail-item"><div class="detail-label">层级深度</div><div class="detail-value">L3</div></div>
        <div class="detail-item"><div class="detail-label">允许父级</div><div class="detail-value">JP_ACQ_KPAY</div></div>
        <div class="detail-item"><div class="detail-label">分户账</div><div class="detail-value">开通</div></div>
        <div class="detail-item full"><div class="detail-label">默认子账户组</div><div class="detail-value">KPay分润户</div></div>
      </div>
      <div class="form-item"><label class="form-label" style="width:auto;padding-right:8px">审核意见（选填）</label>
        <div class="form-content"><textarea class="form-textarea" placeholder="请输入审核意见"></textarea></div>
      </div>
    </div>
    <div class="modal-footer center">
      <button class="btn btn-danger">拒绝</button>
      <button class="btn btn-default" onclick="hideModal(\'m2-audit\')">取消</button>
      <button class="btn btn-primary">通过</button>
    </div>
  </div>
</div>

<!-- ===== M2: 编辑审核对比 ===== -->
<div class="modal" id="m2-edit-audit">
  <div class="modal-dialog" style="width:760px">
    <div class="modal-header"><h3>审核编辑后的实体类型 — Merchant</h3><button class="close-btn" onclick="hideModal(\'m2-edit-audit\')">×</button></div>
    <div class="modal-body">
      <div class="compare-box">
        <div class="compare-panel">
          <div class="compare-title">修改前</div>
          <div class="compare-row"><div class="compare-label">英文实体名称</div><div class="compare-value">Merchant</div></div>
          <div class="compare-row"><div class="compare-label">英文简称</div><div class="compare-value">MERCHANT</div></div>
          <div class="compare-row"><div class="compare-label">实体大类</div><div class="compare-value">下游机构/代理</div></div>
          <div class="compare-row"><div class="compare-label">层级深度</div><div class="compare-value">L4</div></div>
          <div class="compare-row"><div class="compare-label">允许父级</div><div class="compare-value">KPay, Company</div></div>
        </div>
        <div class="compare-panel">
          <div class="compare-title">修改后</div>
          <div class="compare-row"><div class="compare-label">英文实体名称</div><div class="compare-value">Merchant</div></div>
          <div class="compare-row"><div class="compare-label">英文简称</div><div class="compare-value diff">MER <span class="diff-tag">变更</span></div></div>
          <div class="compare-row"><div class="compare-label">实体大类</div><div class="compare-value diff">平台 <span class="diff-tag">变更</span></div></div>
          <div class="compare-row"><div class="compare-label">层级深度</div><div class="compare-value diff">L3 <span class="diff-tag">变更</span></div></div>
          <div class="compare-row"><div class="compare-label">允许父级</div><div class="compare-value diff">KPay <span class="diff-tag">变更</span></div></div>
        </div>
      </div>
      <div class="form-item"><label class="form-label" style="width:auto;padding-right:8px">审核意见（选填）</label>
        <div class="form-content"><textarea class="form-textarea" placeholder="请输入审核意见"></textarea></div>
      </div>
    </div>
    <div class="modal-footer center">
      <button class="btn btn-default">拒绝</button>
      <button class="btn btn-default" onclick="hideModal(\'m2-edit-audit\')">取消</button>
      <button class="btn btn-primary">通过</button>
    </div>
  </div>
</div>

<!-- ===== M2: 详情 ===== -->
<div class="modal" id="m2-detail">
  <div class="modal-dialog" style="width:660px">
    <div class="modal-header"><h3>实体类型详情 — Merchant</h3><button class="close-btn" onclick="hideModal(\'m2-detail\')">×</button></div>
    <div class="modal-body">
      <div class="detail-row">
        <div class="detail-item"><div class="detail-label">业务类型ID</div><div class="detail-value">ACQ</div></div>
        <div class="detail-item"><div class="detail-label">实体类型ID</div><div class="detail-value">JP_ACQ_MERCHANT</div></div>
        <div class="detail-item"><div class="detail-label">英文实体名称</div><div class="detail-value">Merchant</div></div>
        <div class="detail-item"><div class="detail-label">英文简称</div><div class="detail-value">MERCHANT</div></div>
        <div class="detail-item"><div class="detail-label">实体大类</div><div class="detail-value">下游机构/代理</div></div>
        <div class="detail-item"><div class="detail-label">层级深度</div><div class="detail-value">L4</div></div>
        <div class="detail-item"><div class="detail-label">允许父级</div><div class="detail-value">JP_ACQ_KPAY, JP_ACQ_COMPANY</div></div>
        <div class="detail-item"><div class="detail-label">分户账</div><div class="detail-value">开通</div></div>
        <div class="detail-item"><div class="detail-label">审核状态</div><div class="detail-value"><span class="tag tag-pass">审核通过</span></div></div>
        <div class="detail-item"><div class="detail-label">启用状态</div><div class="detail-value">启用</div></div>
      </div>
      <div class="detail-item full" style="width:100%;margin-bottom:12px">
        <div class="detail-label">默认子账户组</div>
        <div class="tag-group">
          <div class="tag-item">KPay交易户</div>
          <div class="tag-item">KPay待结算户</div>
          <div class="tag-item">KPay可提现户</div>
          <div class="tag-item">KPay差错暂记户</div>
        </div>
      </div>
      <div style="font-weight:600;margin-bottom:8px;font-size:13px">操作记录</div>
      <div class="timeline">
        <div class="tl-item"><div class="tl-time">2026-04-11 19:00</div><div class="tl-text">系统初始化创建实体类型</div></div>
        <div class="tl-item"><div class="tl-time">2026-04-11 19:00</div><div class="tl-text">系统管理员审核通过</div></div>
      </div>
    </div>
    <div class="modal-footer right"><button class="btn btn-primary" onclick="hideModal(\'m2-detail\')">关闭</button></div>
  </div>
</div>
'''

P7_MODALS = '''
<!-- ===== M7: 业务场景 新增（完整版含条件+步骤+分录） ===== -->
<div class="modal" id="m7-add">
  <div class="modal-dialog" style="width:1100px">
    <div class="modal-header"><h3>新增业务场景</h3><button class="close-btn" onclick="hideModal(\'m7-add\')">×</button></div>
    <div class="modal-body">
      <div class="section-title" style="margin-top:0">一、基础信息</div>
      <div class="form-row form-row-3" style="margin-bottom:16px">
        <div class="form-item" style="margin-bottom:0"><label class="form-label"><span class="req">*</span>业务场景名称</label>
          <div class="form-content"><input class="form-input" placeholder="例：REFUND"></div>
        </div>
        <div class="form-item" style="margin-bottom:0"><label class="form-label"><span class="req">*</span>业务场景简称</label>
          <div class="form-content"><input class="form-input" placeholder="例：REF"></div>
        </div>
        <div class="form-item" style="margin-bottom:0"><label class="form-label">业务场景ID</label>
          <div class="form-content"><input class="form-input" value="SCE_（自动生成）" disabled><div class="form-tip">格式：SCE_+业务简称</div></div>
        </div>
        <div class="form-item" style="margin-bottom:0"><label class="form-label"><span class="req">*</span>场景大类</label>
          <div class="form-content"><select class="form-select"><option>交易</option><option>对账</option><option>结算</option><option>出款</option></select></div>
        </div>
      </div>
      <div class="divider"></div>
      <div class="section-title">
        二、账务前置触发条件
        <div><button class="btn btn-default btn-sm" onclick="addCond7()">添加条件</button><button class="btn btn-default btn-sm" style="margin-left:6px" onclick="addChildGroup7()">添加子组</button></div>
      </div>
      <div id="m7-cond-root">
        <div class="cond-group">
          <button class="grp-del">×</button>
          <div class="logic-bar">
            <button class="logic-btn logic-and">AND</button>
            <button class="logic-btn logic-or off">OR</button>
            <span class="depth-badge">深度 1/3</span>
          </div>
          <div class="cond-row">
            <span class="drag-h">⠿</span>
            <select class="cond-select" style="width:110px"><option>交易表</option><option>商户表</option></select>
            <select class="cond-select" style="width:130px"><option>支付渠道</option><option>国家码</option><option>交易类型</option><option>支付方式</option></select>
            <select class="cond-select" style="width:80px"><option>等于</option><option>不等于</option><option>属于</option></select>
            <select class="cond-select" style="width:130px"><option>从事件字段取值</option><option>固定值</option></select>
            <input class="cond-input" value="$.transaction_data.channel_id">
            <button class="del-btn" onclick="this.closest(\'.cond-row\').remove()">×</button>
          </div>
        </div>
      </div>
      <div class="divider"></div>
      <div class="section-title">三、业务账户入账<button class="btn btn-primary btn-sm" onclick="addStep7()">新增步骤</button></div>
      <table class="booking-table" id="m7-steps">
        <thead><tr>
          <th>步骤</th><th>业务类型</th><th>实体类型ID</th><th>子账户类型</th><th>单位类型</th><th>单位</th>
          <th>映射字段</th><th>映射类型</th><th>映射值</th><th>金额来源类型</th><th>金额来源值</th><th>操作</th>
        </tr></thead>
        <tbody>
          <tr>
            <td>1</td>
            <td><select class="tbl-select"><option>ACQ</option></select></td>
            <td><select class="tbl-select"><option>JP_ACQ_KPAY</option><option>JP_ACQ_CHANNEL_ADYEN</option><option>JP_ACQ_MERCHANT</option><option>JP_ACQ_STORE</option></select></td>
            <td><select class="tbl-select"><option>KPay交易户</option><option>KPay手续费户</option><option>Adyen通道应收款</option><option>门店交易户</option></select></td>
            <td><select class="tbl-select"><option>CASH</option><option>POINTS</option></select></td>
            <td><select class="tbl-select"><option>JPY</option><option>USD</option><option>HKD</option></select></td>
            <td><select class="tbl-select"><option>支付渠道ID</option><option>KPay商户号</option></select></td>
            <td><select class="tbl-select"><option>从事件字段取值</option><option>固定值</option></select></td>
            <td><input class="tbl-input" value="$.transaction_data.channel_id"></td>
            <td><select class="tbl-select"><option>从事件字段取值</option><option>固定值</option><option>简单表达式</option><option>剩余金额</option></select></td>
            <td><input class="tbl-input" value="$.transaction_data.pay_amount"></td>
            <td><span class="drag-h">⠿</span> <button class="del-btn" onclick="this.closest(\'tr\').remove()">×</button></td>
          </tr>
        </tbody>
      </table>
      <div style="font-size:12px;color:#888;margin-top:4px;margin-bottom:14px">支持拖拽排序</div>
      <div class="divider"></div>
      <div class="section-title">四、会计核心入账<button class="btn btn-primary btn-sm" onclick="addEntry7()">新增分录</button></div>
      <table class="booking-table" id="m7-entries">
        <thead><tr><th>分录</th><th>科目类型</th><th>科目</th><th>借方来源类型</th><th>借方金额/来源值</th><th>贷方来源类型</th><th>贷方金额/来源值</th><th>操作</th></tr></thead>
        <tbody>
          <tr>
            <td>1</td>
            <td><select class="tbl-select" onchange="switchSubject7(this)"><option>资产类</option><option selected>负债类</option><option>损益类</option></select></td>
            <td><select class="tbl-select" style="width:180px"><option>2201-应付商户款-待结算</option></select></td>
            <td><select class="tbl-select"><option>从事件字段取值</option></select></td>
            <td><input class="tbl-input" value="$.transaction_data.pay_amount"></td>
            <td><select class="tbl-select"><option>无</option></select></td>
            <td><input class="tbl-input" placeholder="-"></td>
            <td><button class="del-btn" onclick="this.closest(\'tr\').remove()">×</button></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="modal-footer right">
      <button class="btn btn-default" onclick="hideModal(\'m7-add\')">取消</button>
      <button class="btn btn-default">保存草稿</button>
      <button class="btn btn-primary">提交审核</button>
    </div>
  </div>
</div>

<!-- ===== M7: 新增审核 ===== -->
<div class="modal" id="m7-audit">
  <div class="modal-dialog" style="width:680px">
    <div class="modal-header"><h3>审核业务场景 — REFUND</h3><button class="close-btn" onclick="hideModal(\'m7-audit\')">×</button></div>
    <div class="modal-body">
      <div class="confirm-box"><h4>您确定要审核通过 "REFUND" 吗？</h4><p>业务场景ID：SCE_REFUND &nbsp;&nbsp; 创建人：Sasa</p></div>
      <div class="section-title" style="margin-top:0">基础信息</div>
      <div class="detail-row">
        <div class="detail-item"><div class="detail-label">业务场景名称</div><div class="detail-value">REFUND</div></div>
        <div class="detail-item"><div class="detail-label">业务场景简称</div><div class="detail-value">REF</div></div>
        <div class="detail-item"><div class="detail-label">业务场景ID</div><div class="detail-value">SCE_REFUND</div></div>
        <div class="detail-item"><div class="detail-label">场景大类</div><div class="detail-value">交易</div></div>
      </div>
      <div class="section-title">触发条件</div>
      <div style="background:#f5f7fa;border-radius:6px;padding:10px;font-size:13px;margin-bottom:12px">
        AND：支付渠道 等于 $.transaction_data.channel_id
      </div>
      <div class="section-title">业务账户入账步骤（1步）</div>
      <table class="booking-table">
        <thead><tr><th>步骤</th><th>实体类型ID</th><th>子账户类型</th><th>映射类型</th><th>映射值</th><th>金额来源</th><th>金额来源值</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>JP_ACQ_KPAY</td><td>KPay交易户</td><td>从事件字段取值</td><td>$.channel_id</td><td>从事件字段取值</td><td>$.pay_amount</td></tr>
        </tbody>
      </table>
      <div class="form-item" style="margin-top:14px"><label class="form-label" style="width:auto;padding-right:8px">审核意见（选填）</label>
        <div class="form-content"><textarea class="form-textarea" placeholder="请输入审核意见"></textarea></div>
      </div>
    </div>
    <div class="modal-footer center">
      <button class="btn btn-danger">拒绝</button>
      <button class="btn btn-default" onclick="hideModal(\'m7-audit\')">取消</button>
      <button class="btn btn-primary">通过</button>
    </div>
  </div>
</div>

<!-- ===== M7: 编辑 ===== -->
<div class="modal" id="m7-edit">
  <div class="modal-dialog" style="width:900px">
    <div class="modal-header"><h3>编辑业务场景 — REFUND</h3><button class="close-btn" onclick="hideModal(\'m7-edit\')">×</button></div>
    <div class="modal-body">
      <div class="alert-box alert-orange">编辑业务场景需重新提交审核，审核通过后生效。</div>
      <div class="form-row form-row-3" style="margin-bottom:16px">
        <div class="form-item" style="margin-bottom:0"><label class="form-label"><span class="req">*</span>业务场景名称</label>
          <div class="form-content"><input class="form-input" value="REFUND"></div>
        </div>
        <div class="form-item" style="margin-bottom:0"><label class="form-label">业务场景简称</label>
          <div class="form-content"><input class="form-input" value="REF" disabled></div>
        </div>
        <div class="form-item" style="margin-bottom:0"><label class="form-label">业务场景ID</label>
          <div class="form-content"><input class="form-input" value="SCE_REFUND" disabled></div>
        </div>
      </div>
    </div>
    <div class="modal-footer right">
      <button class="btn btn-default" onclick="hideModal(\'m7-edit\')">取消</button>
      <button class="btn btn-primary">提交审核</button>
    </div>
  </div>
</div>

<!-- ===== M7: 详情 ===== -->
<div class="modal" id="m7-detail">
  <div class="modal-dialog" style="width:680px">
    <div class="modal-header"><h3>业务场景详情 — SALE</h3><button class="close-btn" onclick="hideModal(\'m7-detail\')">×</button></div>
    <div class="modal-body">
      <div class="detail-row">
        <div class="detail-item"><div class="detail-label">业务场景ID</div><div class="detail-value">SCE_SALE</div></div>
        <div class="detail-item"><div class="detail-label">业务场景名称</div><div class="detail-value">SALE</div></div>
        <div class="detail-item"><div class="detail-label">场景大类</div><div class="detail-value">交易</div></div>
        <div class="detail-item"><div class="detail-label">审核状态</div><div class="detail-value"><span class="tag tag-pass">审核通过</span></div></div>
      </div>
      <div class="section-title">触发条件</div>
      <div style="background:#e6f7ff;border-radius:6px;padding:10px;font-size:13px;border-left:3px solid #1890ff;margin-bottom:12px">
        AND：支付渠道 等于 $.transaction_data.channel_id
      </div>
      <div class="section-title">业务账户入账步骤</div>
      <table class="booking-table">
        <thead><tr><th>#</th><th>实体类型ID</th><th>子账户类型</th><th>金额来源</th><th>金额来源值</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>JP_ACQ_CHANNEL_ADYEN</td><td>Adyen通道应收款</td><td>从事件字段</td><td>$.pay_amount</td></tr>
          <tr><td>2</td><td>JP_ACQ_KPAY</td><td>KPay JP 交易户</td><td>从事件字段</td><td>$.pay_amount</td></tr>
        </tbody>
      </table>
      <div class="section-title">会计核心分录</div>
      <table class="booking-table">
        <thead><tr><th>#</th><th>科目代码</th><th>科目名称</th><th>借方金额</th><th>贷方金额</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>1121</td><td>通道应收款</td><td>$.pay_amount</td><td>-</td></tr>
          <tr><td>2</td><td>4601</td><td>手续费收入</td><td>-</td><td>$.transaction_fee</td></tr>
          <tr><td>3</td><td>2201</td><td>应付商户款-待结算</td><td>-</td><td>剩余金额</td></tr>
        </tbody>
      </table>
    </div>
    <div class="modal-footer right"><button class="btn btn-primary" onclick="hideModal(\'m7-detail\')">关闭</button></div>
  </div>
</div>
'''

EXTRA_JS = '''
// ===== P7 helpers =====
function addCond7() {
  const grp = document.querySelector('#m7-cond-root .cond-group');
  if (!grp) return;
  const row = document.createElement('div');
  row.className = 'cond-row';
  row.innerHTML = `<span class="drag-h">⠿</span>
    <select class="cond-select" style="width:110px"><option>交易表</option><option>商户表</option></select>
    <select class="cond-select" style="width:130px"><option>支付渠道</option><option>国家码</option><option>交易类型</option></select>
    <select class="cond-select" style="width:80px"><option>等于</option><option>不等于</option></select>
    <select class="cond-select" style="width:130px"><option>从事件字段取值</option><option>固定值</option></select>
    <input class="cond-input" placeholder="请输入值或字段路径">
    <button class="del-btn" onclick="this.closest('.cond-row').remove()">×</button>`;
  grp.appendChild(row);
}
function addChildGroup7() {
  const root = document.getElementById('m7-cond-root');
  if (!root) return;
  const child = document.createElement('div');
  child.className = 'cond-group child-group';
  child.innerHTML = `<button class="grp-del" onclick="this.closest('.child-group').remove()">×</button>
    <div class="logic-bar">
      <button class="logic-btn logic-and">AND</button>
      <button class="logic-btn logic-or off">OR</button>
      <span class="depth-badge">深度 2/3</span>
    </div>
    <div class="cond-row">
      <span class="drag-h">⠿</span>
      <select class="cond-select" style="width:110px"><option>交易表</option></select>
      <select class="cond-select" style="width:130px"><option>支付渠道</option></select>
      <select class="cond-select" style="width:80px"><option>等于</option></select>
      <select class="cond-select" style="width:130px"><option>固定值</option></select>
      <input class="cond-input" placeholder="请输入值">
      <button class="del-btn" onclick="this.closest('.cond-row').remove()">×</button>
    </div>`;
  root.appendChild(child);
}
function addStep7() {
  const tbody = document.querySelector('#m7-steps tbody');
  if (!tbody) return;
  const idx = tbody.querySelectorAll('tr').length + 1;
  const tr = document.createElement('tr');
  tr.innerHTML = `<td>${idx}</td>
    <td><select class="tbl-select"><option>ACQ</option></select></td>
    <td><select class="tbl-select"><option>JP_ACQ_KPAY</option><option>JP_ACQ_CHANNEL_ADYEN</option><option>JP_ACQ_MERCHANT</option><option>JP_ACQ_STORE</option></select></td>
    <td><select class="tbl-select"><option>KPay交易户</option><option>Adyen通道应收款</option><option>门店交易户</option></select></td>
    <td><select class="tbl-select"><option>CASH</option></select></td>
    <td><select class="tbl-select"><option>JPY</option><option>USD</option></select></td>
    <td><select class="tbl-select"><option>支付渠道ID</option><option>KPay商户号</option></select></td>
    <td><select class="tbl-select"><option>从事件字段取值</option><option>固定值</option></select></td>
    <td><input class="tbl-input" placeholder="$.transaction_data."></td>
    <td><select class="tbl-select"><option>从事件字段取值</option><option>固定值</option><option>简单表达式</option><option>剩余金额</option></select></td>
    <td><input class="tbl-input" placeholder="$.transaction_data.pay_amount"></td>
    <td><span class="drag-h">⠿</span> <button class="del-btn" onclick="this.closest('tr').remove()">×</button></td>`;
  tbody.appendChild(tr);
}
function addEntry7() {
  const tbody = document.querySelector('#m7-entries tbody');
  if (!tbody) return;
  const idx = tbody.querySelectorAll('tr').length + 1;
  const tr = document.createElement('tr');
  tr.innerHTML = `<td>${idx}</td>
    <td><select class="tbl-select" onchange="switchSubject7(this)"><option>资产类</option><option>负债类</option><option>损益类</option></select></td>
    <td><select class="tbl-select" style="width:180px"><option>1121-通道应收款</option><option>2201-应付商户款-待结算</option><option>4601-平台手续费收入</option></select></td>
    <td><select class="tbl-select"><option>从事件字段取值</option><option>固定值</option><option>无</option></select></td>
    <td><input class="tbl-input" placeholder="$.pay_amount"></td>
    <td><select class="tbl-select"><option>无</option><option>从事件字段取值</option><option>固定值</option></select></td>
    <td><input class="tbl-input" placeholder="-"></td>
    <td><button class="del-btn" onclick="this.closest('tr').remove()">×</button></td>`;
  tbody.appendChild(tr);
}
function switchSubject7(sel) {
  const row = sel.closest('tr');
  const sub = row.querySelector('.tbl-select:nth-of-type(2)');
  const t = sel.value;
  if (t === '资产类') sub.innerHTML = '<option>1121-通道应收款</option><option>1122-银行存款</option>';
  else if (t === '负债类') sub.innerHTML = '<option>2201-应付商户款-待结算</option><option>2202-应付商户款-可提现</option><option>2204-争议冻结</option>';
  else sub.innerHTML = '<option>4601-平台手续费收入</option><option>4602-退货手续费收入</option><option>5401-通道手续费支出</option>';
}

// ===== Sidebar nav names update =====
const allPageNames = {
  p1:'业务类型配置', p2:'账户实体配置', p3:'子账户类型配置',
  p4:'单位类型配置', p5:'单位配置', p6:'钱包类型配置',
  p7:'业务场景配置', p8:'入账规则配置', p9:'开户规则配置',
  p10:'激活规则配置', p11:'开户激活事件流水', p12:'账务前置事件流水',
  p13:'开户激活指令流水', p14:'开户激活指令执行', p15:'入账指令流水',
  p16:'入账指令执行流水'
};
'''

# 1. Replace placeholder p1/p2/p7 divs with real content
old_p1 = '<div class="page-view" id="p1"><div class="card"><div class="card-body"><div class="page-title">业务类型配置</div><p style="color:#888;text-align:center;padding:40px">已有完整原型（参见附件1），此处仅作跳转入口展示</p></div></div></div>'
old_p2 = '<div class="page-view" id="p2"><div class="card"><div class="card-body"><div class="page-title">账户实体配置</div><p style="color:#888;text-align:center;padding:40px">已有完整原型（参见附件2），此处仅作跳转入口展示</p></div></div></div>'
old_p7 = '<div class="page-view" id="p7"><div class="card"><div class="card-body"><div class="page-title">业务场景配置</div><p style="color:#888;text-align:center;padding:40px">已有完整原型（参见附件3），此处仅作跳转入口展示</p></div></div></div>'

src = src.replace(old_p1, P1_PAGE)
src = src.replace(old_p2, P2_PAGE)
src = src.replace(old_p7, P7_PAGE)

# 2. Insert modals before </body>
MODALS_BLOCK = P1_MODALS + P2_MODALS + P7_MODALS
src = src.replace('</body>', MODALS_BLOCK + '\n</body>')

# 3. Insert extra JS before </script> closing (last one)
src = src.replace('</script>\n</body>', EXTRA_JS + '\n</script>\n</body>')

# 4. Update sidebar menu labels
old_sidebar_p1 = '<div class="menu-item" onclick="showPage(\'p1\')">业务类型配置</div>'
old_sidebar_p2 = '<div class="menu-item" onclick="showPage(\'p2\')">账户实体配置</div>'
old_sidebar_p7 = '<div class="menu-item" onclick="showPage(\'p7\')">业务场景配置</div>'
# Already have these, just verify they exist
assert old_sidebar_p1 in src, "P1 sidebar not found"

with open('/workspace/account-system-all-prototypes.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"Written: account-system-all-prototypes.html ({len(src)} bytes, ~{len(src.splitlines())} lines)")
