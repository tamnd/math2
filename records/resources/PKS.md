---
records:
    - id: PKS0CG01JZ
      kind: edited-volume
      title: Physics and Mathematics of Link Homology
      creators:
        - name: Sergei Gukov
          role: editor
        - name: Mikhail Khovanov
          role: editor
        - name: Johannes Walcher
          role: editor
      date: "2016-12-23"
      msc:
        - code: 00-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2016-12-23"
          ids:
            doi: 10.1090/conm/680
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2016-12-23"
              ids:
                isbn:
                    - "9781470414597"
                    - "9781470436292"
                    - "9781470436308"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/680
          level: work
        - source: crossref_language
          snapshot: blake3:8055274d703e6bb5b000d2e6eff227662c304b1de00a456a1218f6424b926f45
          native_id: 10.1090/conm/680
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: PKS0M89ZRT
      kind: preprint
      title: 'The role of friction on heave-induced motion of offshore drilling systems: modelling, analysis, and numerical experiments'
      creators:
        - name: Luigi Romano
          role: author
        - name: Ole Morten Aamo
          role: author
      date: "2026-10-15"
      subjects:
        - system: arxiv
          code: physics.app-ph
        - system: arxiv
          code: cs.SY
        - system: arxiv
          code: eess.SY
        - system: arxiv
          code: math.DS
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-15"
          ids:
            arxiv: "2610.22189"
      scope:
        value: out
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.22189"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to out
---
