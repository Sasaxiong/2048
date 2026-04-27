#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Word document for Account System Requirements
"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Page Setup ──────────────────────────────────────────────────────────────
section = doc.sections[0]
section.page_width  = Cm(21.0)
section.page_height = Cm(29.7)
section.left_margin   = Cm(2.5)
section.right_margin  = Cm(2.5)
section.top_margin    = Cm(2.5)
section.bottom_margin = Cm(2.5)

# ── Styles ───────────────────────────────────────────────────────────────────
styles = doc.styles

def set_style(style_name, font_name='Microsoft YaHei', font_size=10.5,
              bold=False, color=None, space_before=0, space_after=4,
              alignment=WD_ALIGN_PARAGRAPH.LEFT):
    try:
        s = styles[style_name]
    except:
        return
    p = s.paragraph_format
    p.space_before = Pt(space_before)
    p.space_after  = Pt(space_after)
    p.alignment    = alignment
    f = s.font
    f.name = font_name
    f.size = Pt(font_size)
    f.bold = bold
    if color:
        f.color.rgb = RGBColor(*color)
    f._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)

# Normal
set_style('Normal', font_size=10.5, space_after=4)

# Custom heading helper
def add_heading(text, level=1, color=(0, 56, 113)):
    p = doc.add_paragraph()
    run = p.add_run(text)
    sz_map = {1: 16, 2: 14, 3: 12, 4: 11}
    run.font.size = Pt(sz_map.get(level, 11))
    run.font.bold = True
    run.font.color.rgb = RGBColor(*color)
    run.font.name = 'Microsoft YaHei'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    if level == 1:
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after  = Pt(6)
        # Bottom border
        pPr = p._p.get_or_add_pPr()
        pBdr = OxmlElement('w:pBdr')
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '6')
        bottom.set(qn('w:space'), '1')
        bottom.set(qn('w:color'), '1890ff')
        pBdr.append(bottom)
        pPr.append(pBdr)
    elif level == 2:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after  = Pt(4)
    elif level == 3:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after  = Pt(3)
    else:
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after  = Pt(2)
    return p

def add_para(text, indent=0, bold_start=None):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.left_indent = Cm(indent)
    p.paragraph_format.space_after = Pt(4)
    if bold_start and text.startswith(bold_start):
        run = p.add_run(bold_start)
        run.font.bold = True
        run.font.size = Pt(10.5)
        run.font.name = 'Microsoft YaHei'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
        rest = text[len(bold_start):]
        if rest:
            run2 = p.add_run(rest)
            run2.font.size = Pt(10.5)
            run2.font.name = 'Microsoft YaHei'
            run2._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    else:
        run = p.add_run(text)
        run.font.size = Pt(10.5)
        run.font.name = 'Microsoft YaHei'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    return p

def add_bullet(text, indent=0.5):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent  = Cm(indent)
    p.paragraph_format.space_after  = Pt(2)
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    run.font.name = 'Microsoft YaHei'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    return p

def set_cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def add_table(headers, rows, col_widths=None, header_bg='1890ff', header_fg=(255,255,255)):
    table = doc.add_table(rows=1+len(rows), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # header row
    hdr = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        set_cell_bg(cell, header_bg)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.bold = True
        run.font.color.rgb = RGBColor(*header_fg)
        run.font.size = Pt(9)
        run.font.name = 'Microsoft YaHei'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    # data rows
    for ri, row_data in enumerate(rows):
        row = table.rows[ri+1]
        if ri % 2 == 0:
            bg = 'f5f9ff'
        else:
            bg = 'ffffff'
        for ci, val in enumerate(row_data):
            cell = row.cells[ci]
            set_cell_bg(cell, bg)
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            run.font.size = Pt(9)
            run.font.name = 'Microsoft YaHei'
            run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    # column widths
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return table

def add_callout(text, box_type='info'):
    colors = {'info': ('e6f7ff','1890ff'), 'warn': ('fff7e6','ff9a2e'),
              'success': ('f6ffed','52c41a'), 'danger': ('fff1f0','ff4d4f')}
    bg, border = colors.get(box_type, colors['info'])
    p = doc.add_paragraph()
    p.paragraph_format.left_indent  = Cm(0.5)
    p.paragraph_format.right_indent = Cm(0.5)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    run = p.add_run(text)
    run.font.size = Pt(9.5)
    run.font.name = 'Microsoft YaHei'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')
    # background shading on paragraph
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), bg)
    pPr.append(shd)
    # left border
    pBdr = OxmlElement('w:pBdr')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:sz'), '12')
    left.set(qn('w:space'), '4')
    left.set(qn('w:color'), border)
    pBdr.append(left)
    pPr.append(pBdr)
    return p

def page_break():
    doc.add_page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  COVER PAGE
# ═════════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(80)
run = p.add_run('外卡收单账户系统\n详细需求文档')
run.font.size = Pt(28)
run.font.bold = True
run.font.color.rgb = RGBColor(0, 56, 113)
run.font.name = 'Microsoft YaHei'
run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p2.paragraph_format.space_before = Pt(20)
run2 = p2.add_run('Account System Detailed Requirements  v2.0')
run2.font.size = Pt(14)
run2.font.color.rgb = RGBColor(100,100,100)
run2.font.name = 'Microsoft YaHei'
run2._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p3.paragraph_format.space_before = Pt(8)
run3 = p3.add_run('参考：Stripe / Adyen / Revolut / Fiserv / Worldpay 设计范式')
run3.font.size = Pt(11)
run3.font.color.rgb = RGBColor(150,150,150)
run3.font.name = 'Microsoft YaHei'
run3._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

meta_items = [
    ('文档版本', 'v2.0'),
    ('编制日期', '2026-04'),
    ('文档状态', '评审中'),
    ('适用系统', '外卡收单 KPay JP'),
]
p4 = doc.add_paragraph()
p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
p4.paragraph_format.space_before = Pt(40)
for k,v in meta_items:
    run4 = p4.add_run(f'  {k}：{v}    ')
    run4.font.size = Pt(10)
    run4.font.color.rgb = RGBColor(80,80,80)
    run4.font.name = 'Microsoft YaHei'
    run4._element.rPr.rFonts.set(qn('w:eastAsia'), 'Microsoft YaHei')

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 1: 文档概述
# ═════════════════════════════════════════════════════════════════════════════
add_heading('一、文档概述', 1)

add_heading('1.1 背景与目标', 2)
add_para('本文档描述外卡收单业务账户系统的完整需求，覆盖从收单通道入账到商户结算出款的全链路。系统以 Stripe 三层抽象模型、Adyen 统一金融引擎、Revolut 多维子账簿、Fiserv 双轨批量架构、Worldpay 双层智能枢纽为参考，结合 KPay 日本业务实际设计。')

add_heading('核心量化目标', 3)
add_table(
    ['目标指标', '要求', '说明'],
    [
        ['年处理交易笔数', '5 亿+（峰值 2000 TPS）', '需支持高并发入账'],
        ['余额查询响应时间', '< 10ms', 'O(1) 索引查询，不扫全表'],
        ['对账准确率', '100%', '分厘不差，差异自动告警'],
        ['支持币种', '36+', '多币种原生支持'],
        ['幂等重试成功率', '99.99%', '三层拦截确保不重复入账'],
        ['系统可用性', '99.95%', '月度不可用时间 < 22分钟'],
    ],
    [4.5, 5, 6.5]
)

add_heading('1.2 系统边界与职责', 2)
add_callout('最重要的边界：账户系统 vs 支付网关\n支付网关负责"能不能付"（验证、授权、路由、委托令牌验证、风控拦截）；账户系统负责"付了怎么记"（入账、记账、维护余额、生成流水）。AI 代理委托令牌验证由支付网关完成，账户系统仅在流水中记录已验证的代理 ID 供审计追溯，不参与验证决策。', 'info')

add_table(
    ['模块', '属于账户系统', '不属于账户系统'],
    [
        ['交易授权', '—', '支付网关（3DS、CVV、欺诈检测）'],
        ['路由决策', '—', '支付网关（智能路由选最优收单通道）'],
        ['入账记录', '✓ 接收已授权交易，执行多步骤入账', '—'],
        ['余额维护', '✓ 维护多维余额索引，防止超提', '—'],
        ['对账', '✓ 与通道报表对账，生成差异处理任务', '—'],
        ['清结算', '✓ 价值日期触发，生成结算单，执行出款', '—'],
        ['AI代理标记', '✓ 在流水中记录 agent_id（已验证信息）', '委托令牌合法性验证（支付网关）'],
        ['配置管理', '✓ 入账规则、分润配置、科目配置', '—'],
    ],
    [3.5, 6, 6.5]
)

add_heading('1.3 核心术语定义', 2)
add_table(
    ['术语', '英文', '定义'],
    [
        ['实体账户', 'Entity Account', '对应法律/业务主体（自有公司、机构、代理、商户、门店）的账户'],
        ['功能子账户', 'Sub-Account', '实体账户下按资金用途划分的账户（交易户、待结算户等），逻辑隔离'],
        ['多维余额索引', 'Balance Index', '按（账户ID + 币种 + 状态维度）建立的余额快速查询索引，O(1) 查询'],
        ['账务前置引擎', 'Pre-Booking Engine', '接收业务事件，按配置规则自动执行多步骤入账的规则引擎'],
        ['会计核心', 'Accounting Core', '执行复式记账，维护科目余额，确保借贷永远平衡的系统模块'],
        ['伞形下沉', 'Umbrella Cascade', '资金从通道应收款逐步流入各层级账户的多步骤入账模式'],
        ['价值日期', 'Value Date', '资金从"在途 PENDING"变为"可用 AVAILABLE"的日期标记'],
        ['暂记账户', 'Suspense Account', '对账差错、待查明资金的临时归集账户，超期必须告警处理'],
        ['清分服务', 'Clearing Service', '按结算周期批量计算分润、生成结算单、触发出款的独立服务'],
        ['辅助核算', 'Auxiliary Accounting', '在科目维度之外增加商户、通道、地区等多维度核算分析能力'],
        ['幂等键', 'Idempotency Key', '防止重复入账的唯一标识：{transaction_id}:{rule_id}:{step_no}:{account_id}'],
    ],
    [3, 4, 9]
)

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 2: 账户模型设计
# ═════════════════════════════════════════════════════════════════════════════
add_heading('二、账户模型设计', 1)

add_heading('2.1 五层实体层次结构', 2)
add_para('系统采用五层实体结构，每层对应不同的业务主体。各层实体独立持有账户，资金在层间流转通过账务前置引擎的伞形下沉步骤实现。')
add_table(
    ['层级', '类型代码', '名称', '典型实体', '默认子账户', '备注'],
    [
        ['L1', 'SELF', '自有公司', 'KPay Japan K.K.', '手续费收入户、差错暂记户、储备金户', '持有收单牌照，账务中心'],
        ['L2', 'INSTITUTION', '机构/收单行', 'Adyen JP、Worldpay JP', '通道应收款户、结算户', '对接外部收单通道'],
        ['L3', 'AGENT', '代理商', '集团A、集团B', '交易户、分润户', '集团管理费从商户抽取'],
        ['L4', 'MERCHANT', '商户', '星巴克JP、麦当劳JP', '交易汇集户、待结算户、可提现户、手续费户、保证金户、争议户', '核心服务对象'],
        ['L5', 'STORE', '门店', '涩谷旗舰店', '交易户', '商户旗下具体门店'],
    ],
    [1.2, 2.5, 2, 3.5, 4, 2.8]
)

add_heading('2.2 功能子账户类型（11种）', 2)
add_para('实体账户与功能类型正交组合，按业务需要为每个实体开通对应的子账户。子账户之间逻辑隔离（通过多维余额索引），非物理独立数据库表。')
add_table(
    ['类型代码', '名称', '适用层级', '资金性质', '允许负余额', '说明'],
    [
        ['CHANNEL_REC', '通道应收款户', 'L2', '资产', '否', '记录从收单通道应收的资金，价值日期前为在途'],
        ['TRADE', '交易汇集户', 'L2/L4', '过渡负债', '否', '伞形下沉的过渡账户，正常情况每日归零'],
        ['PLATFORM_FEE', '平台手续费户', 'L1', '收入', '否', '平台收取的手续费收入归集'],
        ['PENDING', '待结算户', 'L4', '待支付负债', '否', '已确认但价值日期未到的资金；到期自动转可提现户'],
        ['WITHDRAWABLE', '可提现户', 'L4', '可支付负债', '否', '结算完成可立即提现，出款时从此户扣减'],
        ['MERCHANT_FEE', '商户手续费户', 'L4', '费用记录', '否', '商户承担的手续费记录（对账用）'],
        ['DEPOSIT', '保证金户', 'L4', '受限资产', '否', '风控要求的保证金，不计入可提现余额'],
        ['DISPUTE', '争议冻结户', 'L4', '受限资产', '否', '拒付/争议期间冻结；胜诉解冻，败诉划给持卡人'],
        ['SUSPENSE', '差错暂记户', 'L1', '暂记', '技术性是', '对账差错待查明资金临时归集；超T+3未处理自动告警'],
        ['GROUP_FEE', '集团分润户', 'L1/L3', '收入', '否', '集团管理费/代理分润的归集账户'],
        ['RESERVE', '储备金户', 'L1', '风险准备', '否', '平台级风险兜底储备金，应对拒付高峰'],
    ],
    [3, 2.5, 2, 2.5, 2.5, 3.5]
)

add_heading('2.3 多维余额索引模型（核心设计）', 2)
add_callout('设计理念：不采用多个物理子账户表，而使用"主账簿流水（不可变事件溯源）+ 多维余额索引（实时更新）"方案。流水永不修改，状态变更也生成新流水；余额索引按三维实时维护，O(1) 毫秒级查询；快照+增量模式保证期初期末连续。', 'info')

add_heading('余额索引表结构', 3)
add_para('余额索引表以（account_id, currency, dimension）为三维主键，每次余额变动通过 CAS 乐观锁更新：')
add_para('  balance_index(account_id VARCHAR(64), currency VARCHAR(3), dimension VARCHAR(24),', indent=0.5)
add_para('    balance BIGINT DEFAULT 0, version BIGINT DEFAULT 0, last_updated TIMESTAMP)', indent=0.5)
add_para('乐观锁更新条件：version = expected_version AND (delta > 0 OR balance >= |delta|)', indent=0.5)

add_heading('余额维度说明', 3)
add_table(
    ['维度代码', '含义', '计入可用', '触发事件', '解除条件'],
    [
        ['AVAILABLE', '可用余额（可提现）', '✓ 是', '结算完成（SETTLED）', '—'],
        ['PENDING', '在途待结算', '✗ 否', '交易捕获（AUTH_CAPTURED）', '价值日期到达 → 转 AVAILABLE'],
        ['AUTH_HOLD', '预授权占用', '✗ 否', '预授权请求（AUTHORISED）', '捕获→转PENDING；撤销→释放'],
        ['FROZEN_RISK', '风控冻结', '✗ 否', '风控规则触发', '风控审核通过，人工解冻'],
        ['FROZEN_LEGAL', '法律冻结', '✗ 否', '法院命令', '法院撤销冻结令'],
        ['FROZEN_DISPUTE', '争议冻结', '✗ 否', '拒付/争议发起', '争议胜诉解冻；败诉划出'],
        ['SUSPENSE', '暂记待查', '✗ 否', '对账差错发现', '差错查清，完成调账'],
    ],
    [3.5, 3, 1.8, 4, 3.7]
)

add_callout('为什么冻结要分三个维度？\n①解冻条件完全不同：风控冻结需人工审核，法律冻结需法院撤销，争议冻结需争议结案；\n②审计追溯必须区分冻结原因；\n③统计报表需分类分析冻结原因。三个维度共享同一个 balance_index 表，不增加系统复杂度。', 'warn')

add_heading('2.4 账户生命周期', 2)
add_table(
    ['状态', '允许入账', '允许出款/提现', '允许查询', '转换条件'],
    [
        ['待激活', '✗ 否', '✗ 否', '✓ 是', 'KYB通过+配置完成 → 正常'],
        ['正常', '✓ 是', '✓ 是', '✓ 是', '风控触发/人工 → 冻结；申请注销 → 注销流程'],
        ['冻结', '✓ 是（资金只进不出）', '✗ 否', '✓ 是', '审核解冻 → 正常；满足注销条件 → 注销'],
        ['注销', '✗ 否', '✗ 否', '✓ 是（只读）', '终态，不可逆'],
    ],
    [2, 4, 3.5, 2.5, 4]
)

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 3: 资金状态机
# ═════════════════════════════════════════════════════════════════════════════
add_heading('三、资金状态机', 1)

add_heading('3.1 资金状态定义（11种）', 2)
add_table(
    ['状态代码', '名称', '触发事件', '余额索引变化', '可提现'],
    [
        ['AUTHORISED', '预授权成功', '收单通道返回授权码', 'AUTH_HOLD +amount', '✗'],
        ['AUTH_CAPTURED', '预授权完成（捕获）', '商户发起 Capture 请求', 'AUTH_HOLD -amount; PENDING +amount', '✗'],
        ['AUTH_REVERSED', '预授权撤销', '预授权在捕获前撤销', 'AUTH_HOLD -amount', '—'],
        ['CLEARED', '清算完成', '资金到达系统银行账户', '仍在 PENDING，价值日期未到', '✗'],
        ['SETTLED', '结算完成（可用）', '价值日期到达，系统内部结算', 'PENDING -amount; AVAILABLE +amount', '✓'],
        ['PAID_OUT', '已出款', '资金划拨至商户银行账户', 'AVAILABLE -amount', '—'],
        ['FROZEN_RISK', '风控冻结', '风控规则触发，人工确认', 'AVAILABLE -amount; FROZEN_RISK +amount', '✗'],
        ['UNFROZEN_RISK', '风控解冻', '风控审核通过', 'FROZEN_RISK -amount; AVAILABLE +amount', '✓'],
        ['FROZEN_DISPUTE', '争议冻结', '拒付/争议发起', 'AVAILABLE -amount; FROZEN_DISPUTE +amount', '✗'],
        ['DISPUTE_WON', '争议胜诉解冻', '争议结案，商户胜诉', 'FROZEN_DISPUTE -amount; AVAILABLE +amount', '✓'],
        ['DISPUTE_LOST', '争议败诉划出', '争议结案，商户败诉', 'FROZEN_DISPUTE -amount（退持卡人）', '—'],
    ],
    [3.5, 3.5, 4, 4, 1]
)

add_callout('预授权不入账（重要设计决策）\nAUTHORISED 状态仅在余额索引中标记 AUTH_HOLD（防超提），不生成账簿流水，不入账务核心。原因：①预授权可能被撤销，过早入账产生无效流水；②收单通道仅在捕获后确认资金，授权阶段资金未实际转移；③减少流水表数据量。入账从 AUTH_CAPTURED 事件开始。', 'warn')

add_heading('3.2 状态变更核心原则', 2)
add_callout('核心原则：状态变更即流水\n任何状态变更（包括冻结/解冻/结算）均生成一条新的流水记录，原始流水永不修改。这保证了：①任意时刻的余额快照可以通过历史流水完整重建；②期初期末余额始终连续；③审计线索完整。', 'info')

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 4: 账务前置引擎
# ═════════════════════════════════════════════════════════════════════════════
add_heading('四、账务前置引擎', 1)

add_heading('4.1 架构与职责边界', 2)
add_para('账务前置引擎接收业务系统通过消息队列发布的业务事件，根据配置的入账规则，自动执行多步骤的伞形下沉入账流程。')
add_para('处理流程：业务事件发布（MQ）→ 接收事件 → 匹配入账规则 → 执行步骤列表（写入余额索引 + 账簿流水）→ 触发会计核心（写入会计凭证）→ 发布结果事件。')
add_callout('职责边界：支付网关已完成授权验证、委托令牌验证、欺诈检测、路由决策等工作。账务前置引擎只做：入账记录 + 余额更新 + 会计分录生成，不参与任何验证决策。', 'info')

add_heading('4.2 规则配置要素', 2)
add_table(
    ['配置项', '类型', '说明', '示例'],
    [
        ['规则ID', '唯一标识', '规则唯一键，用于幂等键生成', 'RULE_SCE_PURCHASE_JP_ADYEN'],
        ['触发条件', '条件组', 'AND/OR 组合多个字段条件', '事件类型=PURCHASE AND 国家=JP AND 通道=Adyen'],
        ['优先级', '整数', '多规则匹配时，数值越小越优先', '10'],
        ['入账步骤', '步骤列表', '按序执行的子账户变动列表', '6步伞形下沉'],
        ['失败策略', '枚举', '任意步骤失败时的处理方式', 'ROLLBACK_ALL / SUSPEND / SKIP_STEP'],
        ['会计分录模板', '关联', '关联对应的会计凭证模板', 'JE_TPL_PURCHASE'],
        ['幂等键模板', '模板字符串', '防重复入账的唯一键格式', '{txn_id}:{rule_id}:{step_no}:{account_id}'],
    ],
    [3, 2.5, 5.5, 5]
)

add_heading('4.3 步骤配置字段清单', 2)
add_table(
    ['字段名', '必填', '取值方式', '说明'],
    [
        ['子账户类型', '✓', '下拉选择（配置中心枚举）', '目标子账户类型'],
        ['实体类型ID', '✓', '下拉（L1~L5）', '目标实体层级'],
        ['实体ID', '✓', '固定值 / 事件字段路径', '具体实体，如 $.transaction_data.payment_channel'],
        ['方向', '✓', '正向 / 负向', '正向增加余额，负向减少余额'],
        ['变动金额', '✓', '固定值/事件字段/表达式/函数/剩余金额', '本步骤的金额计算规则'],
        ['币种', '✓', '固定值 / 事件字段', '$.transaction_data.currency'],
        ['业务场景ID', '✓', '事件字段', '$.event_metadata.business_scenario_id'],
        ['业务类型', '✓', '事件字段', '$.accounting_data.service_type'],
        ['业务关联ID', '✓', '事件字段', '$.transaction_data.kpay_transaction_id'],
        ['操作类型', '✓', '事件字段', '$.accounting_data.operation_type'],
        ['国家码', '✓', '事件字段', '$.accounting_data.country_code'],
        ['代理ID（AI场景）', '✗', '事件字段（可选）', '$.agent_metadata.agent_id（AI代理发起时填充）'],
    ],
    [4, 1.5, 4.5, 6]
)

add_heading('4.4 金额规则类型', 2)
add_table(
    ['类型', '代码', '示例表达式', '适用场景', '注意'],
    [
        ['事件字段取值', 'EVENT_FIELD', '$.transaction_data.pay_amount', '直接取事件中的原始金额字段', '最常用，性能最佳'],
        ['固定金额', 'FIXED', '5.00', '每笔固定收费', '需关注币种一致性'],
        ['简单表达式', 'EXPRESSION', '$.pay_amount * 0.02', '固定比例计算', '表达式引擎内置支持'],
        ['自定义函数', 'FUNCTION', 'getGroupFeeRate($.merchant_id) * $.pay_amount', '需动态查询配置表的费率', '需开发注册函数，加 Redis 缓存'],
        ['剩余金额', 'REMAINDER', '（系统自动计算）', '最后一步分配所有剩余资金', '只能用于每条规则的最后一步'],
    ],
    [3, 2.5, 5.5, 3.5, 3]
)

add_callout('剩余金额（REMAINDER）的核心价值\n剩余金额 = 最近一次正向入账金额 - 本规则已分配总额。优点：①中间规则变化时最后一步自动适应；②避免浮点精度偏差；③表达"扣完所有费用，剩下都给商户"的业务含义。', 'success')

add_heading('4.5 正向交易入账样例（SCE_PURCHASE）', 2)
add_para('场景：¥100 消费，通道手续费 ¥3，商户净收 ¥97。六步伞形下沉，无负余额。')
add_table(
    ['步骤', '子账户类型', '方向', '变动金额（表达式）', '示例金额', '实体类型ID'],
    [
        ['1', 'Adyen通道应收款', '正向 ↑', '$.transaction_data.pay_amount', '+¥100', '通道（L2）'],
        ['2', 'KPay JP 交易户', '正向 ↑', '$.transaction_data.pay_amount', '+¥100', 'JP_ACQ_KPAY'],
        ['3', 'KPay JP 交易户', '负向 ↓', '$.transaction_data.transaction_fee', '-¥3', 'JP_ACQ_KPAY'],
        ['4', 'KPay JP 手续费户', '正向 ↑', '$.transaction_data.transaction_fee', '+¥3', 'JP_ACQ_KPAY'],
        ['5', 'KPay JP 交易户', '负向 ↓', '$.pay_amount - $.transaction_fee', '-¥97', 'JP_ACQ_KPAY'],
        ['6', '门店交易户', '正向 ↑', '剩余金额', '+¥97', '门店（L5）'],
    ],
    [1.2, 4, 2, 5, 2.5, 3.3]
)
add_callout('步骤逻辑：步骤1确认通道应收资产+100；步骤2 KPay交易户汇集+100；步骤3扣手续费-3；步骤4手续费户确认收入+3；步骤5向下分配-97；步骤6门店落地+97。KPay交易户净变动 = +100-3-97 = 0，过渡账户归零。', 'info')

add_heading('4.6 退货交易入账样例（SCE_REFUND）', 2)
add_para('退货金额 ¥100，额外收退货手续费 ¥3，商户合计退出 ¥103。关键：步骤二先增加 103，确保后续扣减时 KPay 交易户余额始终非负。')
add_table(
    ['步骤', '子账户类型', '方向', '变动金额（表达式）', '示例金额'],
    [
        ['1', 'Adyen通道应收款', '负向 ↓', '$.pay_amount', '-¥100'],
        ['2', 'KPay JP 交易户', '正向 ↑（先增）', '$.pay_amount + $.transaction_fee', '+¥103'],
        ['3', 'KPay JP 交易户', '负向 ↓', '$.transaction_fee', '-¥3'],
        ['4', 'KPay JP 手续费户', '正向 ↑', '$.transaction_fee', '+¥3'],
        ['5', 'KPay JP 交易户', '负向 ↓', '$.pay_amount', '-¥100'],
        ['6', '门店交易户', '负向 ↓', '$.pay_amount + $.transaction_fee', '-¥103'],
    ],
    [1.2, 4, 3, 5.5, 2.5]
)
add_callout('KPay交易户净变动 = +103-3-100 = 0（过渡账户归零）。步骤二先增的设计是"无负余额原则"的关键实现。', 'warn')

add_heading('4.7 集团分润配置', 2)
add_callout('开发实现要求（自定义函数）：在表达式引擎中注册 getGroupFeeRate(merchantId) 函数，根据 merchant_id 查询 group_fee_config 表返回费率。需支持 Redis 缓存（TTL 300秒），配置变更时主动清除缓存。查询不到时返回默认值 0。\n若表达式引擎不支持函数注册，可改用：①配置化 DB_QUERY 类型金额规则；②要求上游在事件中直接传递 $.group_fee_rate 字段（最简方案）。', 'danger')

add_table(
    ['group_fee_config 字段', '类型', '说明'],
    [
        ['group_id', 'VARCHAR(64)', '集团ID（L3代理实体）'],
        ['fee_type', 'VARCHAR(20)', 'RATIO（按比例）| FIXED（固定金额）'],
        ['fee_value', 'DECIMAL(10,6)', '费率(0.02) 或固定金额(5.00)'],
        ['match_type', 'VARCHAR(20)', 'MERCHANT_LIST | MERCHANT_LEVEL | MERCHANT_TAG'],
        ['merchant_ids', 'TEXT', 'JSON数组 ["MCH_001","MCH_002"]'],
        ['effective_date / expiry_date', 'DATE', '生效/失效日期'],
        ['priority', 'INT', '多规则命中时，优先级高的生效'],
    ],
    [5, 3, 8]
)

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 5: 会计核心
# ═════════════════════════════════════════════════════════════════════════════
add_heading('五、会计核心', 1)

add_heading('5.1 科目体系', 2)
add_table(
    ['科目代码', '科目名称', '类型', '辅助核算', '说明'],
    [
        ['1121', '通道应收款', '资产类', '通道', '从收单通道应收的资金，价值日期前为在途'],
        ['1122', '银行存款（聚合账户）', '资产类', '—', '实际资金所在 KPay 银行账户'],
        ['2201', '应付商户款—待结算', '负债类', '商户、通道、地区', '已确认但价值日期未到的商户应收资金'],
        ['2202', '应付商户款—可提现', '负债类', '商户、地区', '结算完成可出款的商户余额'],
        ['2203', '应付集团分润', '负债类', '集团', '清分后应支付给集团的管理费'],
        ['2204', '争议冻结暂记', '负债类', '商户、争议单号', '拒付/争议期间冻结的商户资金'],
        ['2205', '差错暂记账户', '负债类', '差错单号', '对账差错待查明资金的归集科目'],
        ['4601', '平台手续费收入', '收入类', '通道、商户、地区', '平台从每笔交易收取的手续费'],
        ['4602', '退货手续费收入', '收入类', '通道、商户', '退货时额外向商户收取的手续费'],
        ['4603', '集团管理费收入', '收入类', '集团、商户', '集团扣费收入'],
        ['5401', '通道手续费支出', '费用类', '通道', '支付给收单通道的费用'],
        ['6101', '争议损失', '费用类', '商户', '争议败诉产生的损失确认'],
    ],
    [1.8, 4, 2, 4, 4.2]
)

add_heading('5.2 会计分录样例', 2)

add_heading('① 正向交易（¥100消费，手续费¥3）', 3)
add_table(
    ['分录号', '科目', '辅助核算值', '借方（Dr）', '贷方（Cr）', '说明'],
    [
        ['1', '1121 通道应收款', '通道=Adyen', '¥100', '—', '确认应收资产'],
        ['2', '4601 平台手续费收入', '通道=Adyen, 商户=MCH_001', '—', '¥3', '确认手续费收入'],
        ['3', '2201 应付商户款—待结算', '商户=MCH_001, 地区=JP', '—', '¥97', '确认对商户负债'],
        ['合计', '', '', '¥100', '¥100', '✓ 借贷平衡'],
    ],
    [1.5, 5, 4, 2, 2, 2.5]
)

add_heading('② 结算完成分录', 3)
add_table(
    ['分录号', '科目', '借方（Dr）', '贷方（Cr）', '说明'],
    [
        ['1', '1122 银行存款（聚合账户）', '¥100', '—', '资金到账银行'],
        ['2', '1121 通道应收款', '—', '¥100', '核销应收'],
        ['3', '2201 应付商户款—待结算', '¥97', '—', '转出待结算'],
        ['4', '2202 应付商户款—可提现', '—', '¥97', '确认可提现'],
        ['合计', '', '¥197', '¥197', '✓ 借贷平衡'],
    ],
    [1.5, 6, 2, 2, 5]
)

add_heading('③ 退货分录（退¥100，额外手续费¥3）', 3)
add_table(
    ['分录号', '科目', '借方（Dr）', '贷方（Cr）', '说明'],
    [
        ['1', '2202 应付商户款—可提现', '¥103', '—', '商户退回本金+手续费'],
        ['2', '1121 通道应收款（退款）', '—', '¥100', '退款给持卡人'],
        ['3', '4602 退货手续费收入', '—', '¥3', '确认退货手续费收入'],
        ['合计', '', '¥103', '¥103', '✓ 借贷平衡'],
    ],
    [1.5, 6, 2, 2, 5]
)

add_heading('5.3 辅助核算配置', 2)
add_table(
    ['核算类型代码', '核算名称', '值来源', '适用科目', '说明'],
    [
        ['MERCHANT', '商户', '外部表（merchant 表）', '2201、2202、4601', '按商户维度核算收入和负债'],
        ['STORE', '门店', '外部表（store 表）', '2201（可选）', '门店级别的细化核算'],
        ['CHANNEL', '通道', '静态枚举 / 外部API', '1121、4601、5401', '区分 Adyen / Worldpay 等通道'],
        ['REGION', '地区', '静态枚举（JP/HK/SG…）', '2201、4601', '跨国业务按地区核算'],
        ['GROUP', '集团', '外部表（group_entity 表）', '2203、4603', '集团分润的归集核算'],
        ['DISPUTE_NO', '争议单号', '系统生成（UUID）', '2204', '每笔争议独立追踪'],
        ['ERROR_NO', '差错单号', '系统生成（序列号）', '2205', '每笔差错独立追踪'],
    ],
    [3, 2, 4, 3.5, 4.5]
)

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 6: 对账与差错
# ═════════════════════════════════════════════════════════════════════════════
add_heading('六、对账与差错处理', 1)

add_heading('6.1 对账流程', 2)
add_para('对账流程：采集通道报表 → 生成系统快照 → 自动匹配 → 差异识别 → 生成差错单（暂记入账）→ 人工审核 → 对账完成（调账归档）')
add_table(
    ['对账类型', '对账方', '频率', '核对内容', '差异阈值'],
    [
        ['通道对账', 'Adyen/Worldpay 报表文件', '每日凌晨', '交易笔数、交易金额、手续费金额', '0（分厘必查）'],
        ['银行对账', '银行到账流水', '每日', '银行到账金额 vs 系统应收金额', '0'],
        ['会计对账', '总账科目余额', '日终批量', '期末余额 = 期初余额 + 本期借方 - 本期贷方', '0'],
        ['商户对账', '商户自报数据', '每月', '月度结算单与商户确认一致', '待商户确认'],
    ],
    [2.5, 4, 2, 5.5, 2]
)

add_heading('6.2 差错类型与处理机制', 2)
add_callout('核心原则：不修改原始记录，只增加新流水。任何差错处理、调账操作均通过生成新的账簿流水和会计分录实现。原始流水标记为不可变（只读），保证完整的审计线索。', 'warn')
add_table(
    ['差错类型', '识别方式', '发现时处理', '查清后处理'],
    [
        ['平台单边账（系统有，通道无）', '系统交易ID在通道报表缺失', '生成暂记流水：SUSPENSE +amount', '通道确认后补单；或核销冲正'],
        ['通道单边账（通道有，系统无）', '通道报表有，系统无对应记录', '生成入账流水：SUSPENSE +amount', '确认真实交易则补单；否则退回通道'],
        ['金额不一致（两边都有）', '系统金额 ≠ 通道报表金额', '差额进暂记：SUSPENSE +abs(diff)', '与通道协商，收到或退回差额后核销'],
        ['重复入账', '幂等键检测（Redis+DB）', '拦截于入账前，不产生流水；触发告警', '若已入账：人工审核核销冲正'],
        ['退款失败', '通道返回退款失败状态', '资金进差错暂记户', '重新发起/人工打款/系统补偿'],
    ],
    [4, 4.5, 4.5, 3]
)

add_heading('6.3 暂记账户设计', 2)
add_callout('暂记账户是系统的"安全网"：所有无法立即确认归属的资金，先进暂记账户，确保借贷永远平衡。暂记账户余额应每天监控：超 T+3 未处理的自动告警（级别 P1）；超 T+7 上报给财务总监。目标是暂记账户余额趋近于 0。', 'danger')

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 7: 清结算
# ═════════════════════════════════════════════════════════════════════════════
add_heading('七、清结算设计', 1)

add_heading('7.1 结算周期与价值日期', 2)
add_callout('两步解耦设计：\n步骤一（PENDING → AVAILABLE）：由"价值日期到达"事件触发，系统自动执行，与出款频率无关；\n步骤二（AVAILABLE → PAID_OUT）：由"出款指令"触发，按商户配置的出款频率或手动申请执行。\n两步解耦使结算状态准确，出款时机灵活。', 'info')
add_table(
    ['步骤', '触发时机', '余额变化', '会计分录', '执行方式'],
    [
        ['① PENDING → AVAILABLE', '价值日期（Value Date）≤ 今日；默认 T+1', 'PENDING -amount, AVAILABLE +amount', '借：2201 / 贷：2202', '日终批量自动，无需人工'],
        ['② AVAILABLE → PAID_OUT', '结算周期到达（每日/周/月）或手动申请', 'AVAILABLE -amount', '借：2202 / 贷：1122（银行）', '三层审核后执行'],
    ],
    [4, 4.5, 4, 3.5, 3]
)

add_heading('7.2 出款频率配置', 2)
add_table(
    ['出款频率', '说明', '支持条件'],
    [
        ['次日自动', '每个工作日自动出款前一日结算金额', '默认选项，需开通次日达服务'],
        ['每周', '每周五统一出款', '基础服务'],
        ['每月', '每月最后一个工作日出款', '基础服务'],
        ['手动', '商户在可提现余额到达后手动申请', '需满足最低出款金额'],
    ],
    [3, 8, 5]
)

add_heading('7.3 清分服务与账务前置引擎解耦', 2)
add_callout('清分服务与账务前置引擎解耦原则：\n账务前置引擎（交易时实时执行）负责通道入账、手续费记录、商户待结算入账；\n清分服务（结算周期批量执行）负责从待结算资金中扣除集团分润，生成最终可提现余额。\n两者分开的原因：①分润计算依赖历史汇总数据，不适合实时计算；②清分失败不影响交易入账；③结算策略可灵活配置。', 'warn')

add_heading('7.4 三层出款审核模型', 2)
add_table(
    ['层级', '设计', '解决的问题'],
    [
        ['第一层：出款前预览', '系统生成批次预览（汇总+风险摘要），财务点击确认', '心理掌控感，消除对自动化出款的顾虑'],
        ['第二层：异常驱动审核', '风控规则标记可疑交易，进入人工审核池', '异常漏过风险'],
        ['第三层：事后对账', '每日自动生成对账报告，财务核对', '规则错误补救'],
    ],
    [4, 7, 5]
)
add_callout('核心哲学：让机器处理所有符合预期的交易，让人处理不符合预期的例外。', 'success')

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 8: 配置中心
# ═════════════════════════════════════════════════════════════════════════════
add_heading('八、配置中心', 1)

add_heading('8.1 架构设计', 2)
add_callout('模板-实例两层架构：模板（Template）定义配置的结构和字段（元数据），实例（Instance）存储具体的配置值。新增配置类型时只需定义模板，前端根据模板动态渲染表单，无需开发新页面。', 'info')

add_heading('8.2 配置模块一览', 2)
add_table(
    ['配置模块', '包含内容', '数据来源', '更新频率'],
    [
        ['实体类型配置', 'SELF/INSTITUTION/AGENT/MERCHANT/STORE（5种）', '手动配置', '极低'],
        ['子账户类型配置', '11种功能子账户，含余额属性和关联科目', '手动配置', '极低'],
        ['辅助核算配置', '7种核算维度（商户、门店、通道、地区、集团等）', '外部表/静态枚举', '低'],
        ['支付渠道配置', 'Adyen、Worldpay等通道枚举值', '静态枚举/外部API', '低'],
        ['币种配置', '36+种货币，含小数位数', '静态配置', '极低'],
        ['国家/地区配置', '180个国家，含ISO代码', '静态配置', '极低'],
        ['卡品牌配置', 'VISA、MC、AMEX等', '静态配置', '极低'],
        ['触发条件模板', '入账规则的触发条件定义（AND/OR条件组）', '运营人员配置', '中'],
        ['入账步骤模板', '伞形下沉步骤列表（含金额规则）', '运营人员配置', '中'],
        ['会计分录模板', '科目分录行列表（借贷金额规则）', '财务人员配置', '低'],
        ['入账规则管理', '条件模板+步骤模板+分录模板的组合绑定', '运营人员配置', '中'],
        ['科目配置', '科目代码、名称、类型、辅助核算关联', '财务人员配置', '极低'],
        ['集团分润配置', '各集团扣费规则（费率/固定金额/关联商户）', '运营人员配置', '低'],
        ['开户规则配置', '触发条件固定为有新实体记录，配置开哪些子账户和钱包', '运营人员配置', '低'],
        ['激活规则配置', '账户激活的条件组（AND/OR嵌套，最多3层）', '运营人员配置', '低'],
    ],
    [4, 6, 3, 2]
)

add_heading('8.3 开户规则配置说明', 2)
add_callout('开户规则：系统监听实体创建事件（ENTITY_CREATED），一旦检测到新商户/门店记录即自动触发开户流程，无需配置复杂触发条件。主要配置：为哪种实体类型开户、开哪些子账户、创建哪些钱包。审核通过后已选中的子账户类型不可删除，只能新增（保证历史数据完整性）。', 'info')

add_heading('8.4 激活规则配置说明', 2)
add_callout('激活规则：账户创建后默认处于"已创建"状态，需满足激活规则中的条件组后才能变为"已激活"状态，才可以进行入账操作。条件组支持AND/OR 3层嵌套，例如：KYC审核通过 AND 生物识别已通过 AND (合同已签署 OR 豁免批准)。', 'info')

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 9: 并发与幂等
# ═════════════════════════════════════════════════════════════════════════════
add_heading('九、并发控制与幂等性', 1)

add_heading('9.1 三层幂等拦截架构', 2)
add_table(
    ['层级', '机制', '时机', '作用', '失败处理'],
    [
        ['第一层', 'Redis 分布式锁', '事前拦截（最先执行）', '同一幂等键的并发请求只有一个能进入处理', '锁超时或Redis故障时降级到第二层'],
        ['第二层', '数据库唯一约束', '事中拦截（写入时）', '幂等记录表的 idem_key 字段加唯一索引，重复写入抛异常', '捕获DuplicateKeyException，读取历史结果返回'],
        ['第三层', '乐观锁版本号', '逻辑拦截（余额更新）', 'balance_index 的 version 字段，CAS操作防并发超提', 'version不匹配则重试（最多3次），超次数告警'],
    ],
    [2, 3, 3.5, 5, 2.5]
)

add_heading('9.2 幂等键设计', 2)
add_para('幂等键格式：{交易ID}:{规则ID}:{步骤序号}:{账户ID}')
add_para('示例：idem:TXN-20260418-00123:RULE_SCE_PURCHASE_JP_ADYEN:6:ACC_STORE_SBX_NJ01_TRADE', indent=0.5)

add_table(
    ['幂等检测结果', '处理方式', '返回给调用方', '是否重新入账'],
    [
        ['NOT_EXIST', '正常执行入账，创建幂等记录', '200 + 入账结果', '是'],
        ['PROCESSING', '等待锁释放或返回处理中', '202 Accepted', '否'],
        ['SUCCESS', '直接返回历史入账结果，不重复入账', '200 + 历史结果', '否'],
        ['FAILED', '需人工确认后决定是否重试；自动告警', '409 + 错误详情', '需人工确认'],
    ],
    [3, 5.5, 3, 2.5]
)

add_heading('9.3 批量报表并发处理策略', 2)
add_para('月结报告/结算单的并发生成采用以下策略：')
add_bullet('异步任务队列：生成任务放入 MQ（RocketMQ/Kafka），Worker 池异步消费，避免同步阻塞')
add_bullet('数据快照：报表查询 = 日终余额快照 + 当日增量流水，历史月份直接读快照')
add_bullet('任务幂等：每个结算周期维护生成状态字段，防止重复触发')
add_bullet('读库分离：报表查询走只读副本，不影响主库写入')
add_bullet('分页流式输出：超大结果集采用游标分页，避免 OOM')

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 10: 流水管理
# ═════════════════════════════════════════════════════════════════════════════
add_heading('十、流水管理体系', 1)

add_heading('10.1 流水类型总览', 2)
add_table(
    ['流水类型', '描述', '核心字段', '支持操作'],
    [
        ['开户与激活事件流水', '记录 NEW_MERCHANT/KYC_PASSED/BIO_PASSED 等事件的处理结果', '流水ID、事件类型、商户号、处理状态、命中规则、失败原因、重试次数', '查看详情、重试、标记跳过、事件重放'],
        ['账务前置事件流水', '记录每笔交易事件的入账处理结果', '流水ID、业务场景、交易号、商户号、金额、命中规则、步骤执行情况', '查看详情、重试、标记跳过、事件重放'],
        ['开户与激活指令流水', '记录开户/激活指令的生成和状态', '指令ID、指令类型、来源事件ID、商户号、指令内容概要、指令状态', '查看详情、重试、标记跳过、事件重放'],
        ['开户激活指令执行流水', '按步骤记录开户/激活指令的执行过程', '执行流水ID、指令ID、执行步骤、步骤序号、执行参数、执行状态、失败原因', '查看详情、重试、标记跳过'],
        ['业务账户入账指令流水', '记录每个入账步骤生成的业务账户变动指令', '指令ID、交易号、步骤序号、子账户类型、实体ID、方向、金额、幂等键', '查看详情、重试、标记跳过、事件重放'],
        ['业务账户入账执行流水', '记录业务账户余额实际变动的执行结果', '执行流水ID、指令ID、账户ID、执行前余额、变动金额、执行后余额、幂等键', '查看详情、重试、标记跳过'],
        ['会计核心入账指令流水', '记录每个分录生成的会计凭证指令', '指令ID、交易号、凭证号、分录序号、科目代码、借方金额、贷方金额', '查看详情、重试、标记跳过、事件重放'],
        ['会计核心入账执行流水', '记录科目余额实际变动的执行结果', '执行流水ID、指令ID、科目代码、科目名称、借方发生额、贷方发生额、科目余额', '查看详情、重试、标记跳过'],
    ],
    [4.5, 5, 5, 3]
)
add_callout('业务账户入账指令流水与会计核心入账指令流水在界面上通过 Tab 分离展示，但底层共享同一个事件流水 ID，便于跨系统追溯。', 'info')

add_heading('10.2 三种操作说明', 2)
add_table(
    ['操作', '说明', '使用场景', '注意事项'],
    [
        ['重试', '将处理失败的流水重新放入处理队列，按当前规则重新执行', '处理失败次数 < 最大重试次数时，根因已解决（如余额补充、配置修复）', '重试会覆盖之前的失败结果；需确认业务数据已就绪'],
        ['标记跳过', '将流水状态变更为"已跳过"，系统不再自动重试', '人工确认该流水确实无需处理，或已通过其他方式处理', '操作不可撤销；必须填写跳过原因；会保留在审计日志中'],
        ['事件重放', '将原始事件重新推入处理队列，按当前最新规则重新处理', '规则配置变更后需要对历史事件重新处理；数据迁移场景', '使用当前生效规则（非原事件时的规则），可能产生不同结果；需先确认当前规则配置正确'],
    ],
    [2, 5, 5, 4]
)

page_break()

# ═════════════════════════════════════════════════════════════════════════════
#  SECTION 11: 设计决策汇总
# ═════════════════════════════════════════════════════════════════════════════
add_heading('十一、核心设计决策汇总', 1)

add_table(
    ['决策', '选择方案', '放弃方案', '核心理由', '参考来源'],
    [
        ['余额存储方式', '主账簿流水 + 多维余额索引', '物理子账户表', '灵活性：新增状态只加维度；性能：O(1)查询；可追溯：状态变更即流水', 'Stripe/Adyen/Worldpay'],
        ['预授权处理', '仅标记 AUTH_HOLD，不入账', '预授权时入账', '预授权可撤销，过早入账产生无效流水', '业务规则'],
        ['冻结维度', '三个独立维度（RISK/LEGAL/DISPUTE）', '统一FROZEN维度', '解冻条件不同；审计需区分原因；统计报表需分类', 'Worldpay/Adyen'],
        ['状态变更', '生成新流水，原流水只读', '修改原流水', '审计线索完整；期初期末连续；支持任意时刻余额重建', '事件溯源范式'],
        ['退货步骤顺序', '先增后减（步骤二先+103）', '直接负向减少', '伞形账户不允许负余额；先增资金确保后续扣减有效', '本系统设计'],
        ['清分与入账引擎', '清分服务独立，与账务前置引擎解耦', '清分在入账规则中执行', '清分是批量定时，入账是实时；两者失败互不影响', 'Adyen架构'],
        ['集团分润时机', '结算时由清分服务计算', '交易时实时计算', '分润可能需汇总历史；结算策略灵活可配', '业务实践'],
        ['账务系统职责', '入账/记账/余额/流水，不验证/路由', '包含授权验证/路由决策', '职责边界清晰；支付网关已完成所有验证', '架构原则'],
    ],
    [3, 3.5, 3.5, 4, 2]
)

add_heading('待深入设计的模块', 2)
add_table(
    ['模块', '描述', '主要难点', '优先级'],
    [
        ['DCC 多币种设计', '持卡人付GBP，商户收USD的三方货币场景', '双重汇率锁定；分录涉及三种货币', 'P1'],
        ['多层级分润', '机构→代理→平台→商户的N层分润计算', '分润计算图遍历；循环依赖防范；清分性能', 'P1'],
        ['自动化对账引擎', '通道报表采集、解析、自动匹配、差异告警', '各通道报表格式不同；大数据量性能', 'P1'],
        ['月结报告自动化', '月度账单生成、多格式导出、邮件推送', '大数据量快照查询；模板引擎；并发限流', 'P1'],
        ['分库分表策略', '海量账簿流水的分片方案、历史归档', '分片键选择；跨分片查询；冷热数据分离', 'P2'],
        ['AI代理账户扩展', '委托令牌生命周期管理、代理KYB', '委托令牌签发/撤销/过期；边界划分', 'P2'],
        ['灰度发布机制', '入账规则的A/B测试、分阶段上线、自动回滚', '灰度流量控制；双写对比；回滚不影响已入账数据', 'P2'],
        ['保证金动态管理', '基于风险模型动态调整商户保证金水位', '风险模型接入；自动划转触发；合规要求', 'P2'],
    ],
    [4, 5, 4.5, 1.5]
)

# ─── Save ───────────────────────────────────────────────────────────────────
output_path = '/workspace/外卡收单账户系统详细需求文档_v2.docx'
doc.save(output_path)
print(f'Saved: {output_path}')
