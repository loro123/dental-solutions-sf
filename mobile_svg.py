MOBILE_SVG = '''<svg viewBox="0 0 420 1380" xmlns="http://www.w3.org/2000/svg" style="font-family:Calibri,Arial,sans-serif;">
  <defs>
    <!-- Solid arrow (white) -->
    <marker id="mAW" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <!-- Dashed arrow (dim white) -->
    <marker id="mAD" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <!-- Colored arrows -->
    <marker id="mAOrange" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#D85A30" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="mAPink" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#D4537E" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="mAAmber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#BA7517" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="mARed" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#E24B4A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="mAGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#639922" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="mABlue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#378ADD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <!-- =====================================================
       NODE POSITIONS (center-x=210):
       Tongue tie:           y=38..96   center=67
       Jaw underdevelopment: y=136..198 center=167
       Early feeding:        y=238..296 center=267
       Mouth breathing:      y=360..426 center=393
       Tonsils & adenoids:   y=490..548 center=519
       Posture:              y=590..652 center=621
       Disrupted sleep:      y=730..796 center=763
       Overall health:       y=860..936 center=898
       ===================================================== -->

  <!-- =====================================================
       CROSS-CONNECTIONS (drawn first, behind boxes)
       ===================================================== -->

  <!-- 1. Tongue tie → Jaw underdevelopment (curved right side, orange solid) -->
  <path d="M340 67 Q390 67 390 167 Q390 167 340 167" fill="none" stroke="#D85A30" stroke-width="1.5" marker-end="url(#mAOrange)"/>

  <!-- 2. Early feeding → Jaw underdevelopment (curved right side, pink solid) -->
  <path d="M340 267 Q395 267 395 167 Q395 167 340 167" fill="none" stroke="#D4537E" stroke-width="1.5" marker-end="url(#mAPink)"/>

  <!-- 3. Tongue tie dashed feedback loop (left side, down to Jaw) -->
  <path d="M80 67 Q25 67 25 167 Q25 167 80 167" fill="none" stroke="#D85A30" stroke-width="1.2" stroke-dasharray="6 4" marker-end="url(#mAOrange)"/>

  <!-- 4. Mouth breathing → Tonsils (main vertical — drawn as straight, handled below) -->
  <!-- 5. Mouth breathing → Posture (side branch, amber solid) -->
  <path d="M340 393 Q395 393 395 621 Q395 621 340 621" fill="none" stroke="#BA7517" stroke-width="1.5" marker-end="url(#mAAmber)"/>

  <!-- 6. Tonsils → Mouth breathing feedback (dashed loop left side, amber) -->
  <path d="M80 519 Q20 519 20 393 Q20 393 80 393" fill="none" stroke="#BA7517" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#mAAmber)"/>

  <!-- 7. Tonsils → Disrupted sleep (right side, red solid) -->
  <path d="M340 519 Q400 519 400 763 Q400 763 340 763" fill="none" stroke="#E24B4A" stroke-width="1.5" marker-end="url(#mARed)"/>

  <!-- 8. Tonsils dashed feedback loop back to Tongue tie (far left, red dashed) -->
  <path d="M80 490 Q10 490 10 67 Q10 67 80 67" fill="none" stroke="#E24B4A" stroke-width="1.2" stroke-dasharray="6 4" marker-end="url(#mARed)"/>

  <!-- 9. Posture → Disrupted sleep (right side, green solid) -->
  <path d="M340 621 Q405 621 405 763 Q405 763 340 763" fill="none" stroke="#639922" stroke-width="1.5" marker-end="url(#mAGreen)"/>

  <!-- 10. Posture dashed feedback loop to Overall health (far right, green dashed) -->
  <path d="M340 652 Q415 652 415 898 Q415 898 340 898" fill="none" stroke="#639922" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#mAGreen)"/>

  <!-- =====================================================
       VERTICAL MAIN CHAIN ARROWS
       ===================================================== -->

  <!-- Tongue tie → Jaw underdevelopment (main vertical, white) -->
  <path d="M210 96 L210 132" stroke="white" stroke-width="1.5" fill="none" marker-end="url(#mAW)"/>

  <!-- Jaw underdevelopment → Early feeding (main vertical, white) -->
  <path d="M210 198 L210 234" stroke="white" stroke-width="1.5" fill="none" marker-end="url(#mAW)"/>

  <!-- Early feeding → Mouth breathing (main vertical, white, thicker) -->
  <path d="M210 296 L210 356" stroke="white" stroke-width="2" fill="none" marker-end="url(#mAW)"/>

  <!-- Mouth breathing → Tonsils (main vertical, amber solid) -->
  <path d="M210 426 L210 486" stroke="#BA7517" stroke-width="1.5" fill="none" marker-end="url(#mAAmber)"/>

  <!-- Tonsils → Posture (main vertical, white) -->
  <path d="M210 548 L210 586" stroke="white" stroke-width="1.5" fill="none" marker-end="url(#mAW)"/>

  <!-- Posture → Disrupted sleep (main vertical, "forces" label, white) -->
  <path d="M210 652 L210 726" stroke="white" stroke-width="1.5" fill="none" marker-end="url(#mAW)"/>
  <text x="222" y="694" font-size="10" fill="rgba(255,255,255,0.5)" font-style="italic">forces</text>

  <!-- Disrupted sleep → Overall health (main vertical, blue, thicker) -->
  <path d="M210 796 L210 856" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#mABlue)"/>

  <!-- =====================================================
       BOXES & LABELS
       ===================================================== -->

  <!-- ROOT CAUSES label -->
  <text x="210" y="28" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.4)" font-weight="bold" letter-spacing="2">ROOT CAUSES</text>

  <!-- Tongue tie -->
  <rect x="80" y="38" width="260" height="58" rx="12" fill="#D85A30" fill-opacity="0.25" stroke="#D85A30" stroke-opacity="0.7"/>
  <text x="210" y="64" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Tongue tie</text>
  <text x="210" y="82" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Restricted movement</text>

  <!-- Jaw underdevelopment -->
  <rect x="80" y="136" width="260" height="62" rx="12" fill="#7F77DD" fill-opacity="0.25" stroke="#7F77DD" stroke-opacity="0.7"/>
  <text x="210" y="163" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Jaw underdevelopment</text>
  <text x="210" y="181" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Less chewing, narrow palate</text>

  <!-- Early feeding -->
  <rect x="80" y="238" width="260" height="58" rx="12" fill="#D4537E" fill-opacity="0.25" stroke="#D4537E" stroke-opacity="0.7"/>
  <text x="210" y="264" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Early feeding</text>
  <text x="210" y="282" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Breastfeeding, oral function</text>

  <!-- MECHANISM label -->
  <text x="210" y="348" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.4)" font-weight="bold" letter-spacing="2">MECHANISM</text>

  <!-- Mouth breathing -->
  <rect x="70" y="360" width="280" height="66" rx="12" fill="#BA7517" fill-opacity="0.3" stroke="#c9a84c" stroke-width="1.5"/>
  <text x="210" y="388" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Mouth breathing</text>
  <text x="210" y="408" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Bypasses nasal filtration &amp; humidity</text>

  <!-- CONSEQUENCES label -->
  <text x="210" y="480" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.4)" font-weight="bold" letter-spacing="2">CONSEQUENCES</text>

  <!-- Tonsils & adenoids -->
  <rect x="70" y="490" width="280" height="58" rx="12" fill="#A32D2D" fill-opacity="0.3" stroke="#E24B4A"/>
  <text x="210" y="517" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Tonsils &amp; adenoids</text>
  <text x="210" y="535" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Enlarged, obstruct airway</text>

  <!-- Posture -->
  <rect x="70" y="590" width="280" height="62" rx="12" fill="#3B6D11" fill-opacity="0.3" stroke="#639922"/>
  <text x="210" y="617" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Posture</text>
  <text x="210" y="637" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Forward head, neck &amp; shoulder pain</text>

  <!-- IMPACT label -->
  <text x="210" y="720" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.4)" font-weight="bold" letter-spacing="2">IMPACT</text>

  <!-- Disrupted sleep & breathing -->
  <rect x="70" y="730" width="280" height="66" rx="12" fill="#185FA5" fill-opacity="0.3" stroke="#378ADD"/>
  <text x="210" y="758" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Disrupted sleep &amp; breathing</text>
  <text x="210" y="778" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Apnea, snoring, low O&#x2082;</text>

  <!-- OUTCOME label -->
  <text x="210" y="850" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.4)" font-weight="bold" letter-spacing="2">OUTCOME</text>

  <!-- Overall health -->
  <rect x="90" y="860" width="240" height="76" rx="14" fill="#0F6E56" fill-opacity="0.35" stroke="#1D9E75" stroke-width="1.5"/>
  <text x="210" y="892" text-anchor="middle" font-size="14" font-weight="bold" fill="white">Overall health</text>
  <text x="210" y="912" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">Focus, energy, mood,</text>
  <text x="210" y="928" text-anchor="middle" font-size="11" fill="rgba(255,255,255,0.75)">systemic disease risk</text>

  <!-- =====================================================
       LEGEND
       ===================================================== -->
  <text x="210" y="978" text-anchor="middle" font-size="10" fill="rgba(255,255,255,0.35)" font-weight="bold" letter-spacing="2">LEGEND</text>

  <!-- Direct cause -->
  <path d="M90 998 L148 998" stroke="white" stroke-width="1.5" fill="none" marker-end="url(#mAW)"/>
  <text x="158" y="1002" font-size="11" fill="rgba(255,255,255,0.75)">Direct cause</text>

  <!-- Contributing / feedback loop -->
  <path d="M90 1026 L148 1026" stroke="rgba(255,255,255,0.5)" stroke-width="1.5" stroke-dasharray="5 4" fill="none" marker-end="url(#mAD)"/>
  <text x="158" y="1030" font-size="11" fill="rgba(255,255,255,0.75)">Contributing / feedback loop</text>
</svg>'''

if __name__ == '__main__':
    print("Mobile SVG OK, length:", len(MOBILE_SVG))
