---
records:
    - id: DY520CF58X
      kind: preprint
      title: Bandit Phase Retrieval
      creators:
        - name: Tor Lattimore
          role: author
        - name: Botao Hao
          role: author
      date: "2021-06-03"
      subjects:
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.ME
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2021-06-03"
          ids:
            arxiv: "2106.01660"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2106.01660"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: DY5JV2W50N
      kind: edited-volume
      title: Imaging, Multi-scale and High Contrast Partial Differential Equations
      creators:
        - name: Habib Ammari
          role: editor
        - name: Yves Capdeboscq
          role: editor
        - name: Hyeonbae Kang
          role: editor
        - name: Imbo Sim
          role: editor
      date: "2016-03-22"
      msc:
        - code: 35-06
          from: zbmath_search
        - code: 35Bxx
          from: zbmath_search
        - code: 35Jxx
          from: zbmath_search
        - code: 35Rxx
          from: zbmath_search
        - code: 65N15
          from: zbmath_search
        - code: 65T60
          from: zbmath_search
        - code: 00B25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2016-03-22"
          ids:
            doi: 10.1090/conm/660
            zbl: "1343.35005"
            zbl_id: "6576406"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2016-03-22"
              ids:
                isbn:
                    - "9781470419233"
                    - "9781470429324"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/660
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "6576406"
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
