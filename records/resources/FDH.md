---
records:
    - id: FDH8KAXGBR
      kind: course
      title: Topology
      creators:
        - name: P. Veeramani
          role: instructor
      ids:
        course: 03v0r5n49:111106054
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Madras
              ids:
                nptel: "111106054"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106054"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: FDHYD6KAWA
      kind: monograph
      title: Linear and Quasi-linear Equations of Parabolic Type
      creators:
        - name: O. Ladyženskaja
          role: author
        - name: V. Solonnikov
          role: author
        - name: N. Ural′ceva
          role: author
      date: "1968-12-31"
      expressions:
        - key: e1
          kind: edition
          date: "1968-12-31"
          ids:
            doi: 10.1090/mmono/023
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1968-12-31"
              ids:
                isbn:
                    - "9780821815731"
                    - "9780821886533"
                    - "9781470444402"
              access:
                class: record
      relations:
        - kind: part_of
          to: BTDY0N3WC9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/023
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
