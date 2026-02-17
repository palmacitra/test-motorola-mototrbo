#!/usr/bin/env python3
"""
MOTOTRBO Architecture Diagram Generator
Creates professional network topology diagrams for portfolio
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import matplotlib.lines as mlines

# Set style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

def create_capacity_plus_multisite_diagram():
    """Generate Capacity Plus Multi-Site Architecture Diagram"""
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'MOTOTRBO Capacity Plus Multi-Site Architecture', 
            ha='center', fontsize=20, fontweight='bold', color='#0071CE')
    ax.text(8, 9.1, 'Wide-Area Trunked Radio System for Oil & Gas Operations',
            ha='center', fontsize=12, color='#666666')
    
    # Color scheme
    motorola_blue = '#0071CE'
    site_color = '#E8F4F8'
    dispatch_color = '#FFE6E6'
    radio_color = '#E8F8E8'
    
    # Site 1 - NWJ Region
    site1 = FancyBboxPatch((0.5, 5), 5.5, 3.5, 
                           boxstyle="round,pad=0.1", 
                           edgecolor=motorola_blue, 
                           facecolor=site_color, 
                           linewidth=2)
    ax.add_patch(site1)
    ax.text(3.25, 8.2, 'Site 1: North West Java (NWJ)', 
            ha='center', fontsize=11, fontweight='bold')
    ax.text(3.25, 7.8, 'Land-based Oil Production', 
            ha='center', fontsize=9, color='#666666')
    
    # Repeaters Site 1
    for i, pos in enumerate([(1.5, 6.5), (3, 6.5), (4.5, 6.5)]):
        repeater = FancyBboxPatch((pos[0]-0.3, pos[1]-0.25), 0.6, 0.5,
                                  boxstyle="round,pad=0.05",
                                  edgecolor='#333333',
                                  facecolor='white',
                                  linewidth=1.5)
        ax.add_patch(repeater)
        ax.text(pos[0], pos[1], f'R{i+1}', ha='center', va='center', 
                fontsize=8, fontweight='bold')
    
    ax.text(3.25, 5.8, '20 Repeaters | 400 Workers', 
            ha='center', fontsize=9, style='italic')
    
    # Radios Site 1
    for i, pos in enumerate([(1.2, 5.5), (2.2, 5.5), (3.2, 5.5), (4.2, 5.5), (5.2, 5.5)]):
        radio = Circle(pos, 0.15, facecolor=radio_color, edgecolor='#2D7A2D', linewidth=1.5)
        ax.add_patch(radio)
        ax.plot([pos[0], pos[0]], [pos[1]+0.15, pos[1]+0.3], 'k-', linewidth=1)
    
    # Site 2 - SES Region
    site2 = FancyBboxPatch((10, 5), 5.5, 3.5, 
                           boxstyle="round,pad=0.1", 
                           edgecolor=motorola_blue, 
                           facecolor=site_color, 
                           linewidth=2)
    ax.add_patch(site2)
    ax.text(12.75, 8.2, 'Site 2: South East Sumatra (SES)', 
            ha='center', fontsize=11, fontweight='bold')
    ax.text(12.75, 7.8, 'Land + Offshore Platforms', 
            ha='center', fontsize=9, color='#666666')
    
    # Repeaters Site 2
    for i, pos in enumerate([(11, 6.5), (12.5, 6.5), (14, 6.5)]):
        repeater = FancyBboxPatch((pos[0]-0.3, pos[1]-0.25), 0.6, 0.5,
                                  boxstyle="round,pad=0.05",
                                  edgecolor='#333333',
                                  facecolor='white',
                                  linewidth=1.5)
        ax.add_patch(repeater)
        ax.text(pos[0], pos[1], f'R{i+21}', ha='center', va='center', 
                fontsize=8, fontweight='bold')
    
    ax.text(12.75, 5.8, '20 Repeaters | 300 Workers', 
            ha='center', fontsize=9, style='italic')
    
    # Radios Site 2
    for i, pos in enumerate([(10.8, 5.5), (11.8, 5.5), (12.8, 5.5), (13.8, 5.5), (14.8, 5.5)]):
        radio = Circle(pos, 0.15, facecolor=radio_color, edgecolor='#2D7A2D', linewidth=1.5)
        ax.add_patch(radio)
        ax.plot([pos[0], pos[0]], [pos[1]+0.15, pos[1]+0.3], 'k-', linewidth=1)
    
    # IP Backhaul connection
    arrow1 = FancyArrowPatch((6, 6.8), (10, 6.8),
                            arrowstyle='<->', mutation_scale=20, 
                            linewidth=2.5, color=motorola_blue)
    ax.add_patch(arrow1)
    ax.text(8, 7.2, 'IP Network Backhaul', ha='center', fontsize=9, 
            fontweight='bold', color=motorola_blue)
    ax.text(8, 6.95, 'Microwave / Fiber', ha='center', fontsize=8, 
            color='#666666', style='italic')
    
    # Central Dispatch
    dispatch = FancyBboxPatch((5.5, 1.5), 5, 2.8,
                             boxstyle="round,pad=0.15",
                             edgecolor='#CC0000',
                             facecolor=dispatch_color,
                             linewidth=2.5)
    ax.add_patch(dispatch)
    ax.text(8, 4, 'Central Dispatch Control Center', 
            ha='center', fontsize=12, fontweight='bold')
    
    # Dispatch components
    components = [
        ('SmartPTT PLUS', 3.2),
        ('Voice Recording', 2.8),
        ('GPS Tracking', 2.4),
        ('Telephony Gateway', 2.0),
        ('Database Server', 1.6)
    ]
    
    for comp, y in components:
        ax.plot([6.5, 9.5], [y, y], 'k-', linewidth=0.5, alpha=0.3)
        ax.text(6.2, y, '•', fontsize=20, color='#CC0000')
        ax.text(6.5, y, comp, fontsize=9, va='center')
    
    # Connections to dispatch
    arrow2 = FancyArrowPatch((3.25, 5), (7, 4.3),
                            arrowstyle='->', mutation_scale=15,
                            linewidth=2, color='#666666', linestyle='--')
    ax.add_patch(arrow2)
    
    arrow3 = FancyArrowPatch((12.75, 5), (9, 4.3),
                            arrowstyle='->', mutation_scale=15,
                            linewidth=2, color='#666666', linestyle='--')
    ax.add_patch(arrow3)
    
    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=site_color, edgecolor=motorola_blue, 
                      linewidth=2, label='Remote Site (Repeater Infrastructure)'),
        mpatches.Patch(facecolor=dispatch_color, edgecolor='#CC0000', 
                      linewidth=2, label='Central Dispatch & Control'),
        mlines.Line2D([], [], color=motorola_blue, linewidth=2.5, 
                     label='IP Network (Multi-Site Link)'),
        mlines.Line2D([], [], color='#666666', linewidth=2, linestyle='--',
                     label='Control & Monitoring'),
        Circle((0, 0), 0.15, facecolor=radio_color, edgecolor='#2D7A2D', 
              linewidth=1.5, label='Field Radios (Portable/Mobile)')
    ]
    
    ax.legend(handles=legend_elements, loc='upper left', fontsize=8,
             bbox_to_anchor=(0, 0.95), framealpha=0.9)
    
    # System specs box
    specs_box = FancyBboxPatch((0.5, 0.2), 4, 1,
                              boxstyle="round,pad=0.1",
                              edgecolor='#666666',
                              facecolor='#F5F5F5',
                              linewidth=1)
    ax.add_patch(specs_box)
    ax.text(2.5, 1, 'System Specifications', ha='center', 
            fontsize=9, fontweight='bold')
    ax.text(0.7, 0.7, '• Total Repeaters: 40', fontsize=7)
    ax.text(0.7, 0.5, '• Total Users: 700+', fontsize=7)
    ax.text(0.7, 0.3, '• Coverage: Regional', fontsize=7)
    ax.text(2.5, 0.7, '• Technology: DMR Tier III', fontsize=7)
    ax.text(2.5, 0.5, '• Capacity: 3,000 users max', fontsize=7)
    ax.text(2.5, 0.3, '• Trunking: Capacity Plus', fontsize=7)
    
    # Features box
    features_box = FancyBboxPatch((11.5, 0.2), 4, 1,
                                 boxstyle="round,pad=0.1",
                                 edgecolor='#666666',
                                 facecolor='#F5F5F5',
                                 linewidth=1)
    ax.add_patch(features_box)
    ax.text(13.5, 1, 'Key Features', ha='center', 
            fontsize=9, fontweight='bold')
    ax.text(11.7, 0.7, '✓ Automatic Roaming', fontsize=7)
    ax.text(11.7, 0.5, '✓ GPS Tracking', fontsize=7)
    ax.text(11.7, 0.3, '✓ Emergency Priority', fontsize=7)
    ax.text(13.3, 0.7, '✓ Voice Recording', fontsize=7)
    ax.text(13.3, 0.5, '✓ Telephone Interconnect', fontsize=7)
    ax.text(13.3, 0.3, '✓ Man Down Alert', fontsize=7)
    
    plt.tight_layout()
    return fig

def create_ipsc_diagram():
    """Generate IP Site Connect Architecture Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(7, 9.5, 'MOTOTRBO IP Site Connect Architecture', 
            ha='center', fontsize=20, fontweight='bold', color='#0071CE')
    ax.text(7, 9.1, 'Multi-Site Conventional Radio System',
            ha='center', fontsize=12, color='#666666')
    
    motorola_blue = '#0071CE'
    
    # Central router/switch
    router = FancyBboxPatch((5.8, 4.5), 2.4, 1,
                           boxstyle="round,pad=0.1",
                           edgecolor='#CC6600',
                           facecolor='#FFF0E6',
                           linewidth=2.5)
    ax.add_patch(router)
    ax.text(7, 5.2, 'IP Network', ha='center', fontsize=10, fontweight='bold')
    ax.text(7, 4.8, 'WAN/LAN', ha='center', fontsize=8, style='italic')
    
    # Sites arranged in circle
    sites = [
        ('Site 1\nFactory', 2, 7.5, '#E8F4F8'),
        ('Site 2\nWarehouse', 12, 7.5, '#E8F4F8'),
        ('Site 3\nOffice', 2, 1.5, '#E8F4F8'),
        ('Site 4\nPort', 12, 1.5, '#E8F4F8'),
    ]
    
    for site_name, x, y, color in sites:
        # Site box
        site_box = FancyBboxPatch((x-1, y-0.7), 2, 1.4,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=motorola_blue,
                                 facecolor=color,
                                 linewidth=2)
        ax.add_patch(site_box)
        ax.text(x, y+0.4, site_name, ha='center', fontsize=9, fontweight='bold')
        
        # Repeater
        repeater = FancyBboxPatch((x-0.25, y-0.25), 0.5, 0.5,
                                 boxstyle="round,pad=0.05",
                                 edgecolor='#333333',
                                 facecolor='white',
                                 linewidth=1.5)
        ax.add_patch(repeater)
        ax.text(x, y, 'R', ha='center', va='center', fontsize=8, fontweight='bold')
        
        # Connection to router
        if y > 4.5:  # Top sites
            arrow = FancyArrowPatch((x, y-0.7), (7, 5.5),
                                   arrowstyle='<->', mutation_scale=15,
                                   linewidth=2, color=motorola_blue,
                                   linestyle='--', alpha=0.7)
        else:  # Bottom sites
            arrow = FancyArrowPatch((x, y+0.7), (7, 4.5),
                                   arrowstyle='<->', mutation_scale=15,
                                   linewidth=2, color=motorola_blue,
                                   linestyle='--', alpha=0.7)
        ax.add_patch(arrow)
    
    # Legend
    legend_y = 3.2
    ax.text(7, legend_y+0.5, 'System Configuration', ha='center', 
            fontsize=10, fontweight='bold')
    ax.text(7, legend_y+0.2, 'Max 15 Sites | 240 Users per Site', 
            ha='center', fontsize=8)
    ax.text(7, legend_y-0.1, 'Wide-Area Coverage | No Trunking Required', 
            ha='center', fontsize=8, style='italic')
    
    # Feature boxes at bottom
    feature_y = 0.3
    features = [
        ('Cost-Effective', 1.5),
        ('Easy Deployment', 4.5),
        ('Flexible Topology', 7.5),
        ('Scalable Growth', 10.5)
    ]
    
    for feature, fx in features:
        box = FancyBboxPatch((fx-0.8, feature_y-0.15), 1.6, 0.3,
                            boxstyle="round,pad=0.05",
                            edgecolor='#666666',
                            facecolor='#F0F0F0',
                            linewidth=1)
        ax.add_patch(box)
        ax.text(fx, feature_y, feature, ha='center', fontsize=7, fontweight='bold')
    
    plt.tight_layout()
    return fig

def create_repeater_coverage_diagram():
    """Generate Repeater Coverage Planning Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(7, 9.5, 'RF Coverage Planning & Repeater Infrastructure', 
            ha='center', fontsize=20, fontweight='bold', color='#0071CE')
    ax.text(7, 9.1, 'Site Survey and Network Design Methodology',
            ha='center', fontsize=12, color='#666666')
    
    # Coverage circles (overlapping)
    coverage_areas = [
        (3, 5, 2.5, '#0071CE', 'Repeater 1\nSite A', 0.3),
        (7, 5, 2.5, '#00A86B', 'Repeater 2\nSite B', 0.3),
        (11, 5, 2.5, '#CC6600', 'Repeater 3\nSite C', 0.3),
    ]
    
    for x, y, radius, color, label, alpha in coverage_areas:
        coverage = Circle((x, y), radius, facecolor=color, 
                         edgecolor=color, linewidth=2, alpha=alpha)
        ax.add_patch(coverage)
        
        # Repeater tower
        ax.plot([x, x], [y-0.3, y+0.3], color='#333333', linewidth=3)
        ax.plot([x-0.2, x+0.2], [y+0.3, y+0.3], color='#333333', linewidth=2)
        triangle = mpatches.Polygon([[x, y+0.5], [x-0.15, y+0.3], [x+0.15, y+0.3]],
                                   facecolor='red', edgecolor='#333333', linewidth=1)
        ax.add_patch(triangle)
        
        ax.text(x, y-0.6, label, ha='center', fontsize=8, 
                fontweight='bold', color=color)
    
    # Coverage zones
    ax.text(3, 7.8, f'{5} km radius', ha='center', fontsize=7, 
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(7, 7.8, f'{5} km radius', ha='center', fontsize=7,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.text(11, 7.8, f'{5} km radius', ha='center', fontsize=7,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Overlap zones
    ax.text(5, 5, 'Overlap\nZone', ha='center', fontsize=7, 
            style='italic', color='#666666',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    ax.text(9, 5, 'Overlap\nZone', ha='center', fontsize=7,
            style='italic', color='#666666',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    # Planning factors
    factors_box = FancyBboxPatch((0.3, 1), 4.5, 2.5,
                                boxstyle="round,pad=0.15",
                                edgecolor='#666666',
                                facecolor='#F8F8F8',
                                linewidth=1.5)
    ax.add_patch(factors_box)
    ax.text(2.55, 3.2, 'Coverage Planning Factors', ha='center', 
            fontsize=10, fontweight='bold')
    
    planning_items = [
        '• Terrain Analysis (Elevation, Obstacles)',
        '• Path Loss Calculations (Longley-Rice)',
        '• Frequency Coordination & Licensing',
        '• Antenna Height & Gain Optimization',
        '• Power Output Requirements',
        '• Interference Mitigation'
    ]
    
    y_pos = 2.7
    for item in planning_items:
        ax.text(0.6, y_pos, item, fontsize=7, va='top')
        y_pos -= 0.3
    
    # Equipment specs
    specs_box = FancyBboxPatch((9.2, 1), 4.5, 2.5,
                              boxstyle="round,pad=0.15",
                              edgecolor='#666666',
                              facecolor='#F8F8F8',
                              linewidth=1.5)
    ax.add_patch(specs_box)
    ax.text(11.45, 3.2, 'Repeater Specifications', ha='center',
            fontsize=10, fontweight='bold')
    
    specs_items = [
        '• SLR 5000 Series Digital Repeater',
        '• Dual-Slot DMR (2 calls per frequency)',
        '• Output Power: 25-50W',
        '• Antenna: 6-12 dBi gain',
        '• Backup Power: 24-48 hours',
        '• Environmental: IP67 rated'
    ]
    
    y_pos = 2.7
    for item in specs_items:
        ax.text(9.5, y_pos, item, fontsize=7, va='top')
        y_pos -= 0.3
    
    # Network topology option
    ax.text(7, 0.5, 'Topology Options: Single-Site | IP Site Connect | Capacity Plus Multi-Site', 
            ha='center', fontsize=8, style='italic', color='#666666')
    
    plt.tight_layout()
    return fig

# Generate all diagrams
if __name__ == '__main__':
    print("Generating MOTOTRBO Architecture Diagrams...")
    
    # Capacity Plus Multi-Site
    fig1 = create_capacity_plus_multisite_diagram()
    fig1.savefig('/home/claude/motorola-solutions-portfolio/architecture-diagrams/capacity-plus-multisite/capacity-plus-topology.png', 
                 dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created Capacity Plus Multi-Site diagram")
    
    # IP Site Connect
    fig2 = create_ipsc_diagram()
    fig2.savefig('/home/claude/motorola-solutions-portfolio/architecture-diagrams/ip-site-connect/ipsc-topology.png',
                 dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created IP Site Connect diagram")
    
    # Repeater Coverage
    fig3 = create_repeater_coverage_diagram()
    fig3.savefig('/home/claude/motorola-solutions-portfolio/architecture-diagrams/repeater-infrastructure/repeater-coverage.png',
                 dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created Repeater Coverage diagram")
    
    plt.close('all')
    print("\n✓ All diagrams generated successfully!")
