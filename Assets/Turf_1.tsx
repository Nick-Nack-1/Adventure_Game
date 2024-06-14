<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.10.2" name="Turf_1" tilewidth="32" tileheight="32" tilecount="256" columns="16">
 <image source="PathAndObjects.png" width="512" height="512"/>
 <tile id="12">
  <objectgroup draworder="index" id="2">
   <object id="2" x="17" y="17" width="15" height="15"/>
  </objectgroup>
 </tile>
 <tile id="13">
  <objectgroup draworder="index" id="2">
   <object id="2" x="0" y="17" width="32" height="15"/>
  </objectgroup>
 </tile>
 <tile id="14">
  <objectgroup draworder="index" id="2">
   <object id="2" x="0" y="17" width="15" height="15"/>
  </objectgroup>
 </tile>
 <tile id="15">
  <objectgroup draworder="index" id="5">
   <object id="12" x="0" y="0" width="32" height="32"/>
  </objectgroup>
 </tile>
 <tile id="28">
  <objectgroup draworder="index" id="2">
   <object id="4" x="17" y="0" width="15" height="32"/>
  </objectgroup>
 </tile>
 <tile id="29">
  <properties>
   <property name="Collideable" type="bool" value="true"/>
  </properties>
 </tile>
 <tile id="30">
  <objectgroup draworder="index" id="2">
   <object id="4" x="0" y="0" width="15" height="32"/>
  </objectgroup>
 </tile>
 <tile id="44">
  <objectgroup draworder="index" id="2">
   <object id="3" x="17" y="0" width="15" height="15"/>
  </objectgroup>
 </tile>
 <tile id="45">
  <objectgroup draworder="index" id="2">
   <object id="3" x="0" y="0" width="32" height="15"/>
  </objectgroup>
 </tile>
 <tile id="46">
  <objectgroup draworder="index" id="2">
   <object id="2" x="0" y="0" width="15" height="15"/>
  </objectgroup>
 </tile>
 <tile id="60">
  <objectgroup draworder="index" id="2">
   <object id="3" x="0" y="0" width="32" height="15"/>
   <object id="4" x="0" y="0" width="15" height="32"/>
  </objectgroup>
 </tile>
 <tile id="61">
  <objectgroup draworder="index" id="2">
   <object id="4" x="0" y="0" width="32" height="15"/>
   <object id="5" x="17" y="0" width="15" height="32"/>
  </objectgroup>
 </tile>
 <tile id="66" probability="0.1"/>
 <tile id="76">
  <objectgroup draworder="index" id="2">
   <object id="2" x="0" y="17" width="32" height="15"/>
   <object id="3" x="0" y="0" width="15" height="32"/>
  </objectgroup>
 </tile>
 <tile id="77">
  <objectgroup draworder="index" id="2">
   <object id="4" x="0" y="17" width="32" height="15"/>
   <object id="5" x="17" y="0" width="15" height="32"/>
  </objectgroup>
 </tile>
 <wangsets>
  <wangset name="Common" type="corner" tile="-1">
   <wangcolor name="Dirt" color="#ff0000" tile="-1" probability="1"/>
   <wangcolor name="Grass" color="#00ff00" tile="-1" probability="1"/>
   <wangcolor name="Stone" color="#828685" tile="-1" probability="1"/>
   <wangcolor name="Water" color="#0000ff" tile="-1" probability="1"/>
   <wangcolor name="Uprooted" color="#55aa00" tile="-1" probability="1"/>
   <wangtile tileid="0" wangid="0,2,0,3,0,2,0,2"/>
   <wangtile tileid="1" wangid="0,2,0,3,0,3,0,2"/>
   <wangtile tileid="2" wangid="0,2,0,2,0,3,0,2"/>
   <wangtile tileid="6" wangid="0,2,0,1,0,2,0,2"/>
   <wangtile tileid="7" wangid="0,2,0,1,0,1,0,2"/>
   <wangtile tileid="8" wangid="0,2,0,2,0,1,0,2"/>
   <wangtile tileid="9" wangid="0,2,0,1,0,2,0,2"/>
   <wangtile tileid="10" wangid="0,2,0,1,0,1,0,2"/>
   <wangtile tileid="11" wangid="0,2,0,2,0,1,0,2"/>
   <wangtile tileid="12" wangid="0,2,0,4,0,2,0,2"/>
   <wangtile tileid="13" wangid="0,2,0,4,0,4,0,2"/>
   <wangtile tileid="14" wangid="0,2,0,2,0,4,0,2"/>
   <wangtile tileid="15" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="16" wangid="0,3,0,3,0,2,0,2"/>
   <wangtile tileid="17" wangid="0,3,0,3,0,3,0,3"/>
   <wangtile tileid="18" wangid="0,2,0,2,0,3,0,3"/>
   <wangtile tileid="22" wangid="0,1,0,1,0,2,0,2"/>
   <wangtile tileid="23" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="24" wangid="0,2,0,2,0,1,0,1"/>
   <wangtile tileid="25" wangid="0,1,0,1,0,2,0,2"/>
   <wangtile tileid="27" wangid="0,2,0,2,0,1,0,1"/>
   <wangtile tileid="28" wangid="0,4,0,4,0,2,0,2"/>
   <wangtile tileid="30" wangid="0,2,0,2,0,4,0,4"/>
   <wangtile tileid="32" wangid="0,3,0,2,0,2,0,2"/>
   <wangtile tileid="33" wangid="0,3,0,2,0,2,0,3"/>
   <wangtile tileid="34" wangid="0,2,0,2,0,2,0,3"/>
   <wangtile tileid="38" wangid="0,1,0,2,0,2,0,2"/>
   <wangtile tileid="39" wangid="0,1,0,2,0,2,0,1"/>
   <wangtile tileid="40" wangid="0,2,0,2,0,2,0,1"/>
   <wangtile tileid="41" wangid="0,1,0,2,0,2,0,2"/>
   <wangtile tileid="42" wangid="0,1,0,2,0,2,0,1"/>
   <wangtile tileid="43" wangid="0,2,0,2,0,2,0,1"/>
   <wangtile tileid="44" wangid="0,4,0,2,0,2,0,2"/>
   <wangtile tileid="45" wangid="0,4,0,2,0,2,0,4"/>
   <wangtile tileid="46" wangid="0,2,0,2,0,2,0,4"/>
   <wangtile tileid="48" wangid="0,3,0,2,0,3,0,3"/>
   <wangtile tileid="49" wangid="0,3,0,3,0,2,0,3"/>
   <wangtile tileid="50" wangid="0,3,0,3,0,3,0,3"/>
   <wangtile tileid="54" wangid="0,1,0,2,0,1,0,1"/>
   <wangtile tileid="55" wangid="0,1,0,1,0,2,0,1"/>
   <wangtile tileid="56" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="57" wangid="0,5,0,2,0,5,0,5"/>
   <wangtile tileid="58" wangid="0,5,0,5,0,2,0,5"/>
   <wangtile tileid="60" wangid="0,4,0,2,0,4,0,4"/>
   <wangtile tileid="61" wangid="0,4,0,4,0,2,0,4"/>
   <wangtile tileid="64" wangid="0,2,0,3,0,3,0,3"/>
   <wangtile tileid="65" wangid="0,3,0,3,0,3,0,2"/>
   <wangtile tileid="66" wangid="0,3,0,3,0,3,0,3"/>
   <wangtile tileid="70" wangid="0,2,0,1,0,1,0,1"/>
   <wangtile tileid="71" wangid="0,1,0,1,0,1,0,2"/>
   <wangtile tileid="73" wangid="0,2,0,5,0,5,0,5"/>
   <wangtile tileid="74" wangid="0,5,0,5,0,5,0,2"/>
   <wangtile tileid="76" wangid="0,2,0,4,0,4,0,4"/>
   <wangtile tileid="77" wangid="0,4,0,4,0,4,0,2"/>
   <wangtile tileid="89" wangid="0,2,0,5,0,2,0,2"/>
   <wangtile tileid="90" wangid="0,2,0,5,0,5,0,2"/>
   <wangtile tileid="91" wangid="0,2,0,2,0,5,0,2"/>
   <wangtile tileid="92" wangid="0,1,0,3,0,1,0,1"/>
   <wangtile tileid="93" wangid="0,1,0,3,0,3,0,1"/>
   <wangtile tileid="94" wangid="0,1,0,1,0,3,0,1"/>
   <wangtile tileid="105" wangid="0,5,0,5,0,2,0,2"/>
   <wangtile tileid="106" wangid="0,5,0,5,0,5,0,5"/>
   <wangtile tileid="107" wangid="0,2,0,2,0,5,0,5"/>
   <wangtile tileid="108" wangid="0,3,0,3,0,1,0,1"/>
   <wangtile tileid="110" wangid="0,1,0,1,0,3,0,3"/>
   <wangtile tileid="121" wangid="0,5,0,2,0,2,0,2"/>
   <wangtile tileid="122" wangid="0,5,0,2,0,2,0,5"/>
   <wangtile tileid="123" wangid="0,2,0,2,0,2,0,5"/>
   <wangtile tileid="124" wangid="0,3,0,1,0,1,0,1"/>
   <wangtile tileid="125" wangid="0,3,0,1,0,1,0,3"/>
   <wangtile tileid="126" wangid="0,1,0,1,0,1,0,3"/>
   <wangtile tileid="140" wangid="0,3,0,1,0,3,0,3"/>
   <wangtile tileid="141" wangid="0,3,0,3,0,1,0,3"/>
   <wangtile tileid="156" wangid="0,1,0,3,0,3,0,3"/>
   <wangtile tileid="157" wangid="0,3,0,3,0,3,0,1"/>
   <wangtile tileid="163" wangid="0,4,0,4,0,4,0,4"/>
   <wangtile tileid="177" wangid="0,2,0,2,0,2,0,2"/>
  </wangset>
 </wangsets>
</tileset>
