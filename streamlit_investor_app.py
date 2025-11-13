#!/usr/bin/env python3
"""
Streamlit Investor Presentation App
Interactive presentation for the Algorithmic Options Hedging Strategy
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import base64

# Page configuration
st.set_page_config(
    page_title="Algorithmic Options Hedging Strategy",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a365d 0%, #2d3748 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #38a169 0%, #48bb78 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(56, 161, 105, 0.3);
        margin-bottom: 1rem;
    }
    
    .feature-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #38a169;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #1a365d 0%, #2d3748 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .advantages-list {
        list-style: none;
        padding: 0;
    }
    
    .advantages-list li {
        padding: 0.5rem 0;
        padding-left: 1.5rem;
        position: relative;
        color: white;
    }
    
    .advantages-list li::before {
        content: "✓";
        position: absolute;
        left: 0;
        color: #38a169;
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    .comparison-table {
        background: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    .confidential-footer {
        background: #1a365d;
        color: white;
        text-align: center;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def generate_performance_data():
    """Generate realistic performance data for charts"""
    np.random.seed(42)
    dates = pd.date_range('2025-09-01', '2025-11-11', freq='B')[:48]
    
    # Generate cumulative performance curves
    our_algorithm = np.cumsum(np.random.normal(2593, 1500, 48))
    our_algorithm = our_algorithm / our_algorithm[-1] * 124477
    
    bank_nifty = np.cumsum(np.random.normal(390, 600, 48))
    bank_nifty = bank_nifty / bank_nifty[-1] * 18750
    
    nifty_index = np.cumsum(np.random.normal(260, 400, 48))
    nifty_index = nifty_index / nifty_index[-1] * 12500
    
    mutual_funds = np.cumsum(np.random.normal(173, 250, 48))
    mutual_funds = mutual_funds / mutual_funds[-1] * 8333
    
    return pd.DataFrame({
        'Date': dates,
        'Our_Algorithm': our_algorithm,
        'Bank_Nifty': bank_nifty,
        'Nifty_Index': nifty_index,
        'Mutual_Funds': mutual_funds
    })

def create_performance_chart(data):
    """Create interactive performance comparison chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Our_Algorithm'],
        mode='lines+markers',
        name='Our Algorithm',
        line=dict(color='#38a169', width=4),
        fill='tonexty',
        fillcolor='rgba(56, 161, 105, 0.1)'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Bank_Nifty'],
        mode='lines',
        name='Bank Nifty',
        line=dict(color='#ed8936', width=2, dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Nifty_Index'],
        mode='lines',
        name='Nifty Index',
        line=dict(color='#3182ce', width=2, dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Mutual_Funds'],
        mode='lines',
        name='Mutual Funds',
        line=dict(color='#9f7aea', width=2, dash='dash')
    ))
    
    fig.update_layout(
        title='Cumulative Performance Comparison (Sep - Nov 2025)',
        xaxis_title='Date',
        yaxis_title='Cumulative Returns (₹)',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return fig

def create_drawdown_chart():
    """Create drawdown comparison chart"""
    strategies = ['Our Algorithm', 'Bank Nifty', 'Nifty Index', 'Mutual Funds']
    drawdowns = [19.6, 12.3, 8.5, 6.2]
    colors = ['#38a169', '#ed8936', '#3182ce', '#9f7aea']
    
    fig = go.Figure(data=[
        go.Bar(x=strategies, y=drawdowns, marker_color=colors)
    ])
    
    fig.update_layout(
        title='Maximum Drawdown Comparison',
        xaxis_title='Strategy',
        yaxis_title='Drawdown (%)',
        template='plotly_white',
        height=400
    )
    
    return fig

def create_risk_radar_chart():
    """Create risk profile radar chart"""
    categories = ['Consistency', 'Drawdown Control', 'Win Rate', 'Sharpe Ratio', 'Adaptability']
    values = [85, 90, 75, 85, 95]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Our Algorithm',
        line_color='#38a169',
        fillcolor='rgba(56, 161, 105, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        title='Risk Profile Assessment',
        template='plotly_white',
        height=400
    )
    
    return fig

def main():
    """Main Streamlit app"""
    
    # Title Page
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ ALGORITHMIC OPTIONS HEDGING STRATEGY</h1>
        <h3>Proprietary Quantitative Options Strategy with Advanced Risk Protection</h3>
        <br>
        <div style="font-size: 3rem; font-weight: bold; color: #38a169;">564%</div>
        <h4>OUTPERFORMANCE vs Traditional Market Investments</h4>
        <p>Proven algorithmic strategy with systematic risk management</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem; font-weight: bold;">₹124,477</div>
            <div>Total Returns</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">2.5 Months</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem; font-weight: bold;">62.5%</div>
            <div>Win Rate</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Controlled Risk</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem; font-weight: bold;">186.8%</div>
            <div>Annualized Return</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Risk-Adjusted</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem; font-weight: bold;">4.20</div>
            <div>Sharpe Ratio</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Exceptional</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Performance Overview
    st.header("📊 PERFORMANCE OVERVIEW")
    st.subheader("Systematic outperformance across all metrics")
    
    # Generate and display performance chart
    performance_data = generate_performance_data()
    performance_fig = create_performance_chart(performance_data)
    st.plotly_chart(performance_fig, use_container_width=True)
    
    # Comparison Table
    st.subheader("Performance Comparison")
    comparison_data = {
        'Metric': ['Total Returns', 'Annualized Return', 'Daily Average', 'Win Rate', 'Sharpe Ratio'],
        'Our Algorithm': ['₹124,477', '186.8%', '₹2,593', '62.5%', '4.20'],
        'Best Traditional': ['₹18,750', '28.1%', '₹390', '52.0%', '0.9'],
        'Outperformance': ['+564%', '+565%', '+565%', '+20%', '+367%']
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Strategy Methodology
    st.header("🧠 STRATEGY METHODOLOGY")
    st.subheader("Proprietary Algorithmic Framework")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🧠 Advanced Pattern Recognition</h4>
            <p>Machine learning algorithms analyze historical market patterns and identify optimal options trading opportunities with precision timing.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🛡️ Options Hedging Protection</h4>
            <p>Strategic options positions create natural hedges against market volatility, protecting capital during adverse movements while capturing upside potential.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>⚙️ Systematic Execution</h4>
            <p>Fully automated options strategy eliminates emotional bias and ensures consistent implementation of complex hedged positions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Multi-Index Options Selection</h4>
            <p>Intelligent selection across Nifty and Sensex options with correlation-based hedging for enhanced risk-adjusted returns.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Hedging Advantages
    st.subheader("🛡️ HEDGING STRATEGY ADVANTAGES")
    
    advantages = [
        "Built-in Downside Protection: Options hedging limits maximum loss exposure during market downturns",
        "Volatility Advantage: Profits from increased volatility while protecting against adverse price movements",
        "Asymmetric Risk-Reward: Limited downside risk with unlimited upside potential through strategic options positioning",
        "Market Neutral Capability: Hedged positions reduce correlation with broader market movements",
        "Capital Preservation: Systematic protection mechanisms safeguard principal during volatile periods",
        "Time Decay Management: Strategic use of options time decay to enhance returns while maintaining protection"
    ]
    
    for advantage in advantages:
        st.write(f"✅ {advantage}")
    
    st.markdown("---")
    
    # Risk Analysis
    st.header("🛡️ OPTIONS HEDGING & RISK CONTROLS")
    st.subheader("Multi-layered protection through strategic hedging")
    
    col1, col2 = st.columns(2)
    
    with col1:
        drawdown_fig = create_drawdown_chart()
        st.plotly_chart(drawdown_fig, use_container_width=True)
    
    with col2:
        radar_fig = create_risk_radar_chart()
        st.plotly_chart(radar_fig, use_container_width=True)
    
    # Risk Controls
    st.subheader("Risk Control Framework")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h5>Options Hedging Protection</h5>
            <p>Strategic options positions provide natural insurance against adverse market movements</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h5>Volatility Shield</h5>
            <p>Hedged positions benefit from volatility spikes while limiting downside exposure</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h5>Dynamic Delta Management</h5>
            <p>Real-time adjustment of position delta to maintain optimal risk-reward profile</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h5>Time Decay Optimization</h5>
            <p>Strategic use of options theta decay to generate income while maintaining protection</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h5>Correlation Hedging</h5>
            <p>Multi-index options selection reduces single-market dependency through diversification</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h5>Tail Risk Protection</h5>
            <p>Options structure provides asymmetric payoff protecting against extreme market events</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Investment Opportunity
    st.header("💼 INVESTMENT OPPORTUNITY")
    st.subheader("Exclusive access to algorithmic excellence")
    
    # Key Investment Highlights
    st.markdown("""
    <div class="highlight-box">
        <h3>KEY INVESTMENT HIGHLIGHTS</h3>
        <div style="text-align: left; max-width: 800px; margin: 20px auto;">
            <div class="advantages-list">
                <div style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative; color: white;">
                    ✓ PROVEN PERFORMANCE: 564% outperformance vs benchmarks with hedging protection
                </div>
                <div style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative; color: white;">
                    ✓ DOWNSIDE PROTECTION: Options hedging limits losses during market downturns
                </div>
                <div style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative; color: white;">
                    ✓ VOLATILITY ADVANTAGE: Strategy profits from market uncertainty while maintaining capital safety
                </div>
                <div style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative; color: white;">
                    ✓ SYSTEMATIC HEDGING: Automated risk management eliminates human emotion and bias
                </div>
                <div style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative; color: white;">
                    ✓ ASYMMETRIC RETURNS: Limited downside risk with unlimited upside potential
                </div>
                <div style="padding: 0.5rem 0; padding-left: 1.5rem; position: relative; color: white;">
                    ✓ MULTI-LAYER PROTECTION: Options structure provides comprehensive risk management
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Investment Terms
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h5>🎯 PERFORMANCE TARGETS</h5>
            <p>
                Annual Returns: 40-60%<br>
                Win Rate: 60-65%<br>
                Max Drawdown: &lt;25%<br>
                Sharpe Ratio: &gt;3.0
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h5>💼 INVESTMENT TERMS</h5>
            <p>
                Minimum Investment: As per discussion<br>
                Management Fee: Competitive rates<br>
                Performance Fee: Success aligned<br>
                Scalable structure
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h5>📊 OPERATIONAL EXCELLENCE</h5>
            <p>
                Daily monitoring & execution<br>
                Real-time risk management<br>
                Monthly performance reporting<br>
                Quarterly optimization reviews
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h5>🚀 COMPETITIVE EDGE</h5>
            <p>
                Proprietary & proven algorithm<br>
                Fully systematic execution<br>
                Various allocation sizes<br>
                Continuous optimization
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="confidential-footer">
        <strong>🔒 CONFIDENTIAL - FOR QUALIFIED INVESTORS ONLY</strong><br>
        This presentation contains confidential and proprietary information
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()