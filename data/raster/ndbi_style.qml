<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.20.1-Odense" hasScaleBasedVisibilityFlag="0" minScale="1e+08" styleCategories="AllStyleCategories" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal enabled="0" fetchMode="0" mode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <Option type="Map">
      <Option value="false" type="bool" name="WMSBackgroundLayer"/>
      <Option value="false" type="bool" name="WMSPublishDataSourceUrl"/>
      <Option value="0" type="int" name="embeddedWidgets/count"/>
      <Option value="Value" type="QString" name="identify/format"/>
    </Option>
  </customproperties>
  <pipe>
    <provider>
      <resampling maxOversampling="2" enabled="false" zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour"/>
    </provider>
    <rasterrenderer alphaBand="-1" nodataColor="" band="1" opacity="1" classificationMin="-0.4" classificationMax="0.2" type="singlebandpseudocolor">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="1" labelPrecision="4" colorRampType="INTERPOLATED" clip="0" maximumValue="0.2" minimumValue="-0.4">
          <colorramp type="gradient" name="[source]">
            <Option type="Map">
              <Option value="255,255,255,255" type="QString" name="color1"/>
              <Option value="0,42,168,255" type="QString" name="color2"/>
              <Option value="0" type="QString" name="discrete"/>
              <Option value="gradient" type="QString" name="rampType"/>
              <Option value="0.016;253,252,244,255:0.032;251,249,232,255:0.048;249,246,221,255:0.063;247,243,210,255:0.079;244,239,198,255:0.095;242,236,188,255:0.111;243,232,182,255:0.127;243,228,175,255:0.143;243,223,168,255:0.159;242,219,161,255:0.175;242,215,155,255:0.19;242,210,149,255:0.206;243,206,144,255:0.222;243,201,139,255:0.238;244,196,134,255:0.254;244,192,130,255:0.27;244,187,125,255:0.286;244,182,122,255:0.302;245,177,119,255:0.317;245,172,116,255:0.333;245,167,113,255:0.349;245,162,110,255:0.365;245,157,108,255:0.381;245,152,107,255:0.397;245,146,106,255:0.413;244,141,105,255:0.429;244,136,104,255:0.444;243,130,103,255:0.46;243,125,103,255:0.476;241,120,104,255:0.492;240,114,105,255:0.508;239,109,105,255:0.524;237,104,106,255:0.54;236,98,107,255:0.556;234,93,108,255:0.571;231,87,110,255:0.587;229,82,112,255:0.603;226,77,113,255:0.619;224,71,115,255:0.635;221,65,117,255:0.651;217,61,119,255:0.667;213,56,122,255:0.683;209,52,124,255:0.698;205,47,127,255:0.714;200,42,129,255:0.73;196,37,131,255:0.746;190,35,134,255:0.762;184,32,137,255:0.778;178,30,139,255:0.794;172,27,142,255:0.81;166,25,145,255:0.825;159,25,147,255:0.841;151,26,149,255:0.857;143,27,152,255:0.873;134,29,154,255:0.889;125,30,156,255:0.905;116,31,159,255:0.921;105,33,160,255:0.937;92,36,162,255:0.952;79,38,163,255:0.968;63,39,165,255:0.984;41,41,166,255" type="QString" name="stops"/>
            </Option>
            <prop k="color1" v="255,255,255,255"/>
            <prop k="color2" v="0,42,168,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.016;253,252,244,255:0.032;251,249,232,255:0.048;249,246,221,255:0.063;247,243,210,255:0.079;244,239,198,255:0.095;242,236,188,255:0.111;243,232,182,255:0.127;243,228,175,255:0.143;243,223,168,255:0.159;242,219,161,255:0.175;242,215,155,255:0.19;242,210,149,255:0.206;243,206,144,255:0.222;243,201,139,255:0.238;244,196,134,255:0.254;244,192,130,255:0.27;244,187,125,255:0.286;244,182,122,255:0.302;245,177,119,255:0.317;245,172,116,255:0.333;245,167,113,255:0.349;245,162,110,255:0.365;245,157,108,255:0.381;245,152,107,255:0.397;245,146,106,255:0.413;244,141,105,255:0.429;244,136,104,255:0.444;243,130,103,255:0.46;243,125,103,255:0.476;241,120,104,255:0.492;240,114,105,255:0.508;239,109,105,255:0.524;237,104,106,255:0.54;236,98,107,255:0.556;234,93,108,255:0.571;231,87,110,255:0.587;229,82,112,255:0.603;226,77,113,255:0.619;224,71,115,255:0.635;221,65,117,255:0.651;217,61,119,255:0.667;213,56,122,255:0.683;209,52,124,255:0.698;205,47,127,255:0.714;200,42,129,255:0.73;196,37,131,255:0.746;190,35,134,255:0.762;184,32,137,255:0.778;178,30,139,255:0.794;172,27,142,255:0.81;166,25,145,255:0.825;159,25,147,255:0.841;151,26,149,255:0.857;143,27,152,255:0.873;134,29,154,255:0.889;125,30,156,255:0.905;116,31,159,255:0.921;105,33,160,255:0.937;92,36,162,255:0.952;79,38,163,255:0.968;63,39,165,255:0.984;41,41,166,255"/>
          </colorramp>
          <item value="-0.4" color="#ffffff" alpha="255" label="-0.4000"/>
          <item value="-0.3904" color="#fdfcf4" alpha="255" label="-0.3904"/>
          <item value="-0.3808" color="#fbf9e8" alpha="255" label="-0.3808"/>
          <item value="-0.3712" color="#f9f6dd" alpha="255" label="-0.3712"/>
          <item value="-0.3622" color="#f7f3d2" alpha="255" label="-0.3622"/>
          <item value="-0.3526" color="#f4efc6" alpha="255" label="-0.3526"/>
          <item value="-0.343" color="#f2ecbc" alpha="255" label="-0.3430"/>
          <item value="-0.3334" color="#f3e8b6" alpha="255" label="-0.3334"/>
          <item value="-0.3238" color="#f3e4af" alpha="255" label="-0.3238"/>
          <item value="-0.3142" color="#f3dfa8" alpha="255" label="-0.3142"/>
          <item value="-0.3046" color="#f2dba1" alpha="255" label="-0.3046"/>
          <item value="-0.295" color="#f2d79b" alpha="255" label="-0.2950"/>
          <item value="-0.286" color="#f2d295" alpha="255" label="-0.2860"/>
          <item value="-0.2764" color="#f3ce90" alpha="255" label="-0.2764"/>
          <item value="-0.2668" color="#f3c98b" alpha="255" label="-0.2668"/>
          <item value="-0.2572" color="#f4c486" alpha="255" label="-0.2572"/>
          <item value="-0.2476" color="#f4c082" alpha="255" label="-0.2476"/>
          <item value="-0.238" color="#f4bb7d" alpha="255" label="-0.2380"/>
          <item value="-0.2284" color="#f4b67a" alpha="255" label="-0.2284"/>
          <item value="-0.2188" color="#f5b177" alpha="255" label="-0.2188"/>
          <item value="-0.2098" color="#f5ac74" alpha="255" label="-0.2098"/>
          <item value="-0.2002" color="#f5a771" alpha="255" label="-0.2002"/>
          <item value="-0.1906" color="#f5a26e" alpha="255" label="-0.1906"/>
          <item value="-0.181" color="#f59d6c" alpha="255" label="-0.1810"/>
          <item value="-0.1714" color="#f5986b" alpha="255" label="-0.1714"/>
          <item value="-0.1618" color="#f5926a" alpha="255" label="-0.1618"/>
          <item value="-0.1522" color="#f48d69" alpha="255" label="-0.1522"/>
          <item value="-0.1426" color="#f48868" alpha="255" label="-0.1426"/>
          <item value="-0.1336" color="#f38267" alpha="255" label="-0.1336"/>
          <item value="-0.124" color="#f37d67" alpha="255" label="-0.1240"/>
          <item value="-0.1144" color="#f17868" alpha="255" label="-0.1144"/>
          <item value="-0.1048" color="#f07269" alpha="255" label="-0.1048"/>
          <item value="-0.0952" color="#ef6d69" alpha="255" label="-0.0952"/>
          <item value="-0.0856" color="#ed686a" alpha="255" label="-0.0856"/>
          <item value="-0.076" color="#ec626b" alpha="255" label="-0.0760"/>
          <item value="-0.0664" color="#ea5d6c" alpha="255" label="-0.0664"/>
          <item value="-0.0574" color="#e7576e" alpha="255" label="-0.0574"/>
          <item value="-0.0478" color="#e55270" alpha="255" label="-0.0478"/>
          <item value="-0.0382" color="#e24d71" alpha="255" label="-0.0382"/>
          <item value="-0.0286" color="#e04773" alpha="255" label="-0.0286"/>
          <item value="-0.019" color="#dd4175" alpha="255" label="-0.0190"/>
          <item value="-0.00939999999999996" color="#d93d77" alpha="255" label="-0.0094"/>
          <item value="0.000200000000000033" color="#d5387a" alpha="255" label="0.0002"/>
          <item value="0.00980000000000009" color="#d1347c" alpha="255" label="0.0098"/>
          <item value="0.0188" color="#cd2f7f" alpha="255" label="0.0188"/>
          <item value="0.0284" color="#c82a81" alpha="255" label="0.0284"/>
          <item value="0.038" color="#c42583" alpha="255" label="0.0380"/>
          <item value="0.0476" color="#be2386" alpha="255" label="0.0476"/>
          <item value="0.0572" color="#b82089" alpha="255" label="0.0572"/>
          <item value="0.0668000000000001" color="#b21e8b" alpha="255" label="0.0668"/>
          <item value="0.0764000000000001" color="#ac1b8e" alpha="255" label="0.0764"/>
          <item value="0.0860000000000001" color="#a61991" alpha="255" label="0.0860"/>
          <item value="0.095" color="#9f1993" alpha="255" label="0.0950"/>
          <item value="0.1046" color="#971a95" alpha="255" label="0.1046"/>
          <item value="0.1142" color="#8f1b98" alpha="255" label="0.1142"/>
          <item value="0.1238" color="#861d9a" alpha="255" label="0.1238"/>
          <item value="0.1334" color="#7d1e9c" alpha="255" label="0.1334"/>
          <item value="0.143" color="#741f9f" alpha="255" label="0.1430"/>
          <item value="0.1526" color="#6921a0" alpha="255" label="0.1526"/>
          <item value="0.1622" color="#5c24a2" alpha="255" label="0.1622"/>
          <item value="0.1712" color="#4f26a3" alpha="255" label="0.1712"/>
          <item value="0.1808" color="#3f27a5" alpha="255" label="0.1808"/>
          <item value="0.1904" color="#2929a6" alpha="255" label="0.1904"/>
          <item value="0.2" color="#002aa8" alpha="255" label="0.2000"/>
          <rampLegendSettings suffix="" direction="0" useContinuousLegend="1" orientation="2" maximumLabel="" prefix="" minimumLabel="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option value="" type="QChar" name="decimal_separator"/>
                <Option value="6" type="int" name="decimals"/>
                <Option value="0" type="int" name="rounding_type"/>
                <Option value="false" type="bool" name="show_plus"/>
                <Option value="true" type="bool" name="show_thousand_separator"/>
                <Option value="false" type="bool" name="show_trailing_zeros"/>
                <Option value="" type="QChar" name="thousand_separator"/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" gamma="1" contrast="0"/>
    <huesaturation colorizeOn="0" colorizeRed="255" grayscaleMode="0" colorizeGreen="128" colorizeStrength="100" saturation="0" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
