---
records:
    - id: 4KT9TK3MG4
      kind: preprint
      title: Optimal Parameter-Free Second-order Acceleration with Inexact Hessians under Generalized Smoothness
      creators:
        - name: Artem Agafonov
          role: author
        - name: Aslan Ashabokov
          role: author
        - name: Alexander D'yakonov
          role: author
        - name: Martin Takáč
          role: author
        - name: Alexander Gasnikov
          role: author
        - name: Dmitry Kamzolov
          role: author
      date: "2026-09-26"
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-26"
          ids:
            arxiv: "2609.32977"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.32977"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: 4KTQH6TNWD
      kind: monograph
      title: 'Fluid Dynamics and Linear Elasticity: A First Course in Continuum Mechanics'
      creators:
        - name: Michael S. Ruderman
          role: author
      date: "2019"
      expressions:
        - key: e1
          kind: edition
          date: "2019"
          ids:
            doi: 10.1007/978-3-030-19297-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2019"
              ids:
                isbn:
                    - "9783030192969"
                    - "9783030192976"
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-19297-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
