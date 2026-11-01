---
records:
    - id: XDBS24FM0F
      kind: edited-volume
      title: 'Council for African American Researchers in the Mathematical Sciences: Volume III'
      creators:
        - name: Alfred G. Noël
          role: editor
        - name: Earl Barnes
          role: editor
        - name: Sonya A. F. Stephens
          role: editor
      date: "2001"
      msc:
        - code: 00B20
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2001"
          ids:
            doi:
                - 10.1090/conm/275
                - 10.1090/conm/467
            zbl: "0964.00028"
            zbl_id: "1616041"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2001"
              ids:
                isbn:
                    - "9780821821411"
                    - "9780821856116"
                    - "9780821878651"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2008"
              ids:
                isbn:
                    - "9780821844571"
                    - "9780821857953"
                    - "9780821881460"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/275
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/467
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1616041"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
