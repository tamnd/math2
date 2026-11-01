---
records:
    - id: MWMAGBQ7QQ
      kind: problem-set
      title: Kvant 2021, no. 9
      creators:
        - name: Kvant editorial board
          role: editor
      date: "2021"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "2021"
          structure: MWMAGBQ7QQ/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2021-9
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
    - id: MWMR4VATED
      kind: monograph
      title: Elementary Algebraic Geometry
      creators:
        - name: Klaus Hulek
          role: author
      date: "2003-02-13"
      msc:
        - code: 14-01
          from: zbmath_search
        - code: 14Hxx
          from: zbmath_search
        - code: 14Jxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2003-02-13"
          ids:
            doi: 10.1090/stml/020
            zbl: "1022.14001"
            zbl_id: "1886504"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2003-02-13"
              ids:
                isbn:
                    - "9781470421342"
                    - "9780821829523"
              access:
                class: record
      relations:
        - kind: part_of
          to: 6RX4VMGQKK
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/stml/020
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1886504"
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
