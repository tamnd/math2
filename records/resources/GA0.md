---
records:
    - id: GA02GNB9AA
      kind: monograph
      title: Tensor Categories
      creators:
        - name: Pavel Etingof
          role: author
        - name: Shlomo Gelaki
          role: author
        - name: Dmitri Nikshych
          role: author
        - name: Victor Ostrik
          role: author
      date: "2015-07-22"
      msc:
        - code: 18-02
          from: zbmath_search
        - code: 16T05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2015-07-22"
          ids:
            doi: 10.1090/surv/205
            zbl: "1365.18001"
            zbl_id: "6444410"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2015-07-22"
              ids:
                isbn:
                    - "9781470420246"
                    - "9781470423490"
              access:
                class: record
      relations:
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/205
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "6444410"
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
